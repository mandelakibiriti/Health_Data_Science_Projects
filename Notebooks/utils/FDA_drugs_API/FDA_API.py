import os, ast, logging, requests, json
import pandas as pd
from functools import reduce
from urllib.request import urlopen
from urllib.error import HTTPError
from collections import defaultdict

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')

'''
DATA FETCHING FROM FDA ENDPOINTS
'''
# Limit per query is 1000 items in json Object
# Get classifications of medication from 3 base endpoints - drugsfda / label / ndc
# https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/

url_list = ['label', 'ndc', 'drugsfda']
base_file = r'../FDA_drugs_API/csv_pharma_data/'

try:
    list_df = []
    for str_url in url_list:
        url = str('https://api.fda.gov/drug/') + str_url + str('.json?count=openfda.pharm_class_epc.exact')
        api_obj = urlopen(url).read() # read as byte type
        dict_drug_class = ast.literal_eval(api_obj.decode('utf-8'))
        class_list = [val for res in dict_drug_class.items() for val in res[1] if type(val) is dict]
        # Convert to dataframe and save to csv
        # Uncomment to save json obj to csv
        drug_class_index = pd.DataFrame(class_list)
        data_csv = drug_class_index.to_csv(base_file + str_url + '.csv')
        # Combine dataframes in a list
        list_df.append(drug_class_index)
    # Merge dataframes
    df = reduce(lambda df1,df2: pd.merge(df1, df2, how='left', on='term'), list_df)
    df.columns = ['term', 'label', 'ndc', 'drugsfda']
    df.to_csv(base_file + 'merged_endpoints.csv')
        
except HTTPError as err:
    print('The error code: %s \nUrl as: %s' % (err, err.filename))

# Script to get JSON per drug class uncomment to fetch data
# Iterating through pandas objects is generally slow. 
# In many cases, iterating manually over the rows is not needed and can be avoided
# https://dataindependent.com/pandas/pandas-iterate-over-rows-5-methods/
print('Fetching Data......')
drug_obj_list = []
# File location
csv_base_file = r'../FDA_drugs_API/csv_pharma_data/'
file_ext = '.csv'

# Change url endpoint eg. label.json / drugsfda.json / ndc.json
base_url = 'https://api.fda.gov/drug/'
end_url = '.json?search=openfda.pharm_class_epc:"'
limit = '&limit='
next_page = '&skip='

# Folder location to save json files
base_directory = os.getcwd()
data_base_file = base_directory + "/pharma_data/"
try:
    for index in range(len(url_list)):
        route = url_list[index]
        full_route = pd.read_csv(csv_base_file + route + file_ext)
        
        for pos, drug_class in full_route.iterrows(): 
            class_term = drug_class['term']
            class_count = drug_class['count']
            if class_count > 1000:
                while class_count > 1000:
                    class_count -= 1000
                    drug_class_url =  base_url + route + end_url + str(class_term) + '"' + next_page + str(class_count) + limit + str(1000)
                    if class_count < 1000:
                        drug_class_url =  base_url + route + end_url + str(class_term) + '"' + limit + str(class_count)
                        continue 
            else:
                drug_class_url =  base_url + route + end_url + str(class_term) + '"' + limit + str(class_count)

            print('Data parsed from: %s using endpoint %s' % (class_term, route),'\n', drug_class_url)
            print('Processing Data......')

            # logging.info('Data parsed from: %s using endpoint %s' % (class_term, route),'\n', drug_class_url)
            # logging.info('Processing Data......')

            # using requests because urlopen doesn't handle the multiple string variables in drug_class_url
            drug_class_obj = requests.get(drug_class_url)
            if drug_class_obj.status_code >= 200 and drug_class_obj.status_code <= 299:
                dict_drug_class_json = json.loads(drug_class_obj.content) # ast.literal_eval throws ValueError for complex string
            else:
                logging.error('Error in fetching data from url:', drug_class_url)
            for item in dict_drug_class_json.items():
                # Corticosteroid [4], Anti-epileptic Agent [1], Azole Antifungal [1], Polyene Antifungal[1], Antifibrinolytic Agent [2] missing items
                # TODO: create a error function to get len of items and match and throw an error if match not present
                # print('Length of json is: %s' %(len(item[1])) ) returns a tuple
                for items in item[1]:
                    if type(items) is dict:
                        drug_obj_list.append(items)
        # save data into json
        with open( route + '.json', 'w', encoding='utf-8') as f:
            json.dump(drug_obj_list, f)
        print(
            "------------------------\n Data from %s saved as json" % route
            )
    index += 1
except HTTPError as err:
    logging.info(class_term)
    logging.error('The error code: %s \nUrl as: %s' % (err, err.filename))

'''
DATA SORTING AND PROCESSING
'''
# data needed from various endpoints
drug_info_list= []
# data not matching pattern selection
rejected_drug_list = []

# Switch case for various keys
def getDosage():
    # dosage exception
    if 'active_ingredients' in drug_keys:
        dosage = item['active_ingredients'][0]['strength']
    elif 'products' in drug_keys:
        list_dosages = item['products'][0]['active_ingredients']
        length_list = len(list_dosages)
        if length_list > 1:
            dosage_list = [items['strength'] for items in list_dosages if 'strength' in items ]
            dosage = ' + '.join(dosage_list)  
        else:
            dosage = list_dosages[0]['strength']
    else:
        dosage = 'Dosage not available on FDA API'
    return dosage

def getApplicationNumber():
    try:
        # application_number exception
        if 'application_number' in drug_keys:
            application_no = item['application_number']
        elif 'openfda' in drug_keys:
            if 'application_number' in item['openfda']:
                application_no = item['openfda']['application_number'][0]
            else:
                application_no = item['openfda']['product_ndc']
        elif 'product_ndc' in drug_keys:
            application_no = item['product_ndc']
    except:
        application_no = 'Application Number not available on FDA API'
         # use the product_ndc number if application number not available
    return application_no

def getPharmClass():
    # pharm_class exception
    if 'openfda' in drug_keys:
        pharm_class = item['openfda']['pharm_class_epc']
    elif 'pharm_class' in drug_keys:
        # gets last index which correlates to CS field
        pharm_class = item['pharm_class'][-1]
    else:
        pharm_class = 'Pharm Class not available on FDA API'
    return pharm_class

def getPharmMoA():
    # pharm_moa exception
    try:
        if 'openfda' in drug_keys:
            pharm_moa = item['openfda']['pharm_class_moa']
    except:
        pharm_moa = 'MoA not available on FDA API'
    return pharm_moa

def getRoute():
    # route exception
    try:
        if 'openfda' in drug_keys:
            if 'route' in item['openfda']:
                drug_route = item['openfda']['route'][0]
            else:
                drug_route = item['route'][0]
        elif 'products' in drug_keys:
            drug_route = item['products'][0]['route'][0]
    except:
        drug_route = 'Route not available on FDA API'
    return drug_route

def getDosageForm():
    # dosage_form exception
    if 'dosage_form' in drug_keys:
        dosage_form = item['dosage_form']
    elif 'products' in drug_keys:
        dosage_form = item['products'][0]['dosage_form']
    else:
        dosage_form = 'Dosage Form not available on FDA API'
    return dosage_form

def getDrugName():
    # drug_name exception
    try:
        if 'active_ingredients' in drug_keys:
            drug_name = item['active_ingredients'][0]['name']
        # 'products' key only used in OPENFDA ENDPOINT
        elif 'products' in drug_keys:
            list_names = item['products'][0]['active_ingredients']
            list_length = len(list_names)
            if list_length > 1:
                drug_list_name = [items['name'] for items in list_names if 'name' in items]
                drug_name = ','.join(drug_list_name)
            else:
                drug_name = list_names[0]['name']
        elif 'generic_name' in drug_keys:
            # generic name exception
            drug_name = item['generic_name']
        elif 'openfda' in drug_keys:
            drug_name = item['openfda']['generic_name'][0]
    except:
            drug_name = 'Drug Name not available on FDA API'
    return drug_name

def getProductType():
    try:
        # product_type exception
        if 'openfda' in drug_keys:
            if 'product_type' in item['openfda']:
                product_type = item['openfda']['product_type']
            else:
                product_type = item['product_type']
        elif 'product_type' in drug_keys:
            product_type = item['product_type']
    except:
        product_type = 'Product Type not available on FDA API'
    return product_type

# Analyze the json file with respect only to ndc and drugsfda endpoint which has data
# that mainly match the fields needed for the merged json
file_list = ['ndc', 'drugsfda']
for i in range(len(file_list)):
    # Run range to open files individually
    file_url = file_list[i] + '.json'
    f = open(file_url)
    drug_json = json.load(f)
    logging.info('Json data loaded')
    
    # Clean data based on methods
    for item in drug_json:  
        try:
            drug_pos = drug_json.index(item)
            # openfda json dict has most of the info in all endpoints
            # but lacks certain fields and exception errors need to handled
            drug_keys = item.keys()
            application_no = getApplicationNumber()
            drug_name = getDrugName()
            drug_class = getPharmClass()
            drug_moa = getPharmMoA()
            drug_route = getRoute()
            drug_dosage_form = getDosageForm()
            drug_dosage = getDosage()
            drug_type = getProductType()
            drug_manufacturer_name = item['openfda']['manufacturer_name']

            #print(
            #    'Drug added: %s with application number: %s under class: %s at position: %s\n' % 
            #    (drug_name, application_no, drug_class, drug_pos)
            #    )  

            # Summarize data per drug
            drug_data = [drug_pos, drug_route, drug_dosage_form, drug_dosage, drug_type, drug_class, drug_moa, drug_manufacturer_name]
            drug_info_dict = {drug_name: drug_data}
            drug_info_list.append(drug_info_dict)
        
        except Exception or KeyError as err:
            rejected_drug_data = [drug_pos, drug_route, drug_dosage_form, drug_type, drug_class, drug_moa, drug_manufacturer_name]
            rejected_drug_dict = {drug_name: rejected_drug_data}
            logging.exception(err)
            logging.info(
                'Error in: %s with application number: %s under class: %s at position: %s because of: %s\n' % 
                (drug_name, application_no, drug_class, drug_pos, err) 
                )
            rejected_drug_list.append(rejected_drug_dict)

    logging.info('Processing data......')
    with open(r'../FDA_drugs_API/pharmacy_' + file_list[i] + '.json', 'w') as f:
        json.dump(drug_info_list, f)

    with open(r'../FDA_drugs_API/reject_data_' + file_list[i] + '.json', 'w') as f:
        json.dump(rejected_drug_list, f)
    logging.info('Data processed')

'''
DATA CLEANING AND MERGE IN ONE JSON
'''
def merge_json():
    # urls for json files - label endpoint data not 
    # used as doesn't have majority of required fields
    files = [
        r'../FDA_drugs_API/pharmacy_ndc.json',
        r'../FDA_drugs_API/pharmacy_drugsfda.json'
    ]
    # list of merged json
    merge_json = []

    # read each json url and merge json
    for file in files:
        with open(file, 'r') as inFile:
            merge_json.extend(json.load(inFile))

    # sort and merge json in alphabetical order as well as group
    # each drug is a dict item
    # {'IBUPROFEN': [0, 'ORAL', 'CAPSULE, LIQUID FILLED', '200 mg/1', 'HUMAN OTC DRUG', 
    #   ['Nonsteroidal Anti-inflammatory Drug [EPC]'], ['Cyclooxygenase Inhibitors [MoA]'], ['Safeway, Inc.']]
    # }
    sorted_json = sorted(merge_json, key = str) 
    arranged_json = defaultdict(list)
    # Group Drugs under same drug name
    for item in sorted_json:
        for k,v in sorted(item.items()):
            arranged_json[k].append(v)
    
    # write into single json file
    with open(r'../FDA_drugs_API/merge.json','w') as outFile:
        json.dump(arranged_json, outFile)
    
    # extract items in list using recursion
    def extract_list(item):
        for key, value in item.items():
            # converts nested array items into tuples
            for val in value:
                for i in range(len(val)):
                    if type(val[i]) is list:
                        val[i] = tuple(val[i])
            # convert primary arrays in nested arrays as tuples
            tuple_items = [tuple(list_items) for list_items in value]
            # carry out set to remove duplicates
            new_val = sorted(set(list(tuple_items)), key = tuple_items.index)
            arranged_json[key] = new_val
    # run method on arranged_json object        
    extract_list(arranged_json)

    # write into single json file
    with open(r'../FDA_drugs_API/final.json','w') as outFile:
        json.dump(arranged_json, outFile)

final_json = merge_json()
