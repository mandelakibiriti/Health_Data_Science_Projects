# OPENFDA API JSON FETCH
[openFDA API](https://open.fda.gov/apis/drug/) api is an Elasticsearch-based API that serves public FDA data about nouns like drugs, devices, and foods. The endpoints are periodically updated with new information.

The current script works to acquire data from the drugs API endpoint as a json file which has 3 endpoints:
1. [labels endpoint](https://open.fda.gov/apis/drug/label/)
   > Drug manufacturers and distributors submit documentation about their products to FDA in the Structured Product Labeling (SPL) format. The openFDA drug product labeling API returns data from this dataset. 
2. [drugsfda endpoint](https://open.fda.gov/apis/drug/drugsfda/)
   > Contains information about the following FDA-approved products for human use: Prescription brand-name drug products, generic drug products, and many therapeutic biological products Over-the-counter brand-name and generic drugs.
3. [ndc endpoint](https://open.fda.gov/apis/drug/ndc/)
   > Contains a current list of all drugs manufactured, prepared, propagated, compounded, or processed by it for commercial distribution.

# Working with the FDA_API.py script
The endpoints are changed and specified in the key areas of the script:
> Loading of csv files
```
drugsfda_csv = pd.read_csv('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/csv_pharma_data/openfda.csv')
label_csv = pd.read_csv('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/csv_pharma_data/label.csv')
ndc_csv = pd.read_csv('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/csv_pharma_data/ndc.csv')
```
> Highlighting url to be used
```
base_url = 'https://api.fda.gov/drug/ndc.json?search=openfda.pharm_class_epc:"'
```
> Determing csv to be used in loop for key search
```
for pos, drug_class in ndc_csv.iterrows():
```
> Specifying writing and reading of respective preliminary json data file
```
# Write JSON file
with open('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/pharm_data/pharma_data_ndc.json', 'w') as f:

# Read JSON file
f = open('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/pharma_data/pharma_data_ndc.json')
```

> Writing final cleaned data file
```
with open('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/pharmacy_ndc.json', 'w') as f:
    json.dump(drug_info_list, f)

with open('../Automate-Queries-Migrations-to-GraphCMS/Drug_ICD APIs/reject_data_ndc.json', 'w') as f:
    json.dump(rejected_drug_list, f)
```
# Structure of data fetched from API based on specified endpoint
1. Data has been structured as list of dictionaries as follows with corresponding iteration:
   - drug name -> ```key```
   - position in json -> ```drugs[key][0]```
   - route of administration -> ```drugs[key][1]```
   - dosage -> ```drugs[key][2]``` 
   - type of drug (over the counter or prescription drug) -> ```drugs[key][3]``` 
   - classification [EPC] -> ```drugs[key][4]```
   - mechanism of action [MoA] -> ```drugs[key][5]```
   - manufacturer name -> ```drugs[key][6]```
```
{
        "IBUPROFEN": [
            0,
            "ORAL",
            "CAPSULE, LIQUID FILLED",
            "200 mg/1",
            "HUMAN OTC DRUG",
            [
                "Nonsteroidal Anti-inflammatory Drug [EPC]"
            ],
            [
                "Cyclooxygenase Inhibitors [MoA]"
            ],
            [
                "Safeway, Inc."
            ]
        ]
    }
```
2. For data not available in the specific API end point a string is parsed : `[Field] not available on FDA API`
```
{
    "NAPROXEN": [
        0,
        "ORAL",
        "Dosage Form not available on FDA API",
        "Dosage not Available on FDA API",
        [
            "HUMAN PRESCRIPTION DRUG"
        ],
        [
            "Nonsteroidal Anti-inflammatory Drug [EPC]"
        ],
        [
            "Cyclooxygenase Inhibitors [MoA]"
        ],
        [
            "A-S Medication Solutions"
        ]
    ]
}
```
3. Merged data based on number of entries based on drug name
```
".ALPHA.-BISABOLOL, (+/-)-": [
        [
            14926,
            "TOPICAL",
            "CREAM",
            ".5 g/100mL",
            "HUMAN OTC DRUG",
            [
                "Adenosine Receptor Agonist [EPC]"
            ],
            [
                "Adenosine Receptor Agonists [MoA]"
            ],
            [
                "rootsallo Qwell"
            ]
        ],
        [
            14927,
            "TOPICAL",
            "CREAM",
            ".5 g/100mL",
            "HUMAN OTC DRUG",
            [
                "Adenosine Receptor Agonist [EPC]"
            ],
            [
                "Adenosine Receptor Agonists [MoA]"
            ],
            [
                "rootsallo Qwell"
            ]
        ]
    ]
```