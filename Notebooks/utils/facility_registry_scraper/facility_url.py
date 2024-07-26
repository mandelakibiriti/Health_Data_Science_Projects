import logging
import pandas as pd

from urllib.request import Request
from selenium import webdriver
from selenium.webdriver.common.by import By

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

driver = webdriver.Chrome()
facility_registry = pd.read_excel("KMPDC_Facility_URLs.xlsx")    

facility_list = []

for index, facility in facility_registry.iterrows():
    # Iterate over data frame to get urls
    url = facility["View"]
    # Visit page on each url
    page_req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    driver.get(url)
    # Get input values
    input = driver.find_elements(By.CLASS_NAME, "form-control")
    facility_details = [ i.get_attribute("value") for i in input]
    # print(facility_details)
    facility_list.append(facility_details)
    # print(facility_list)
    if type(url) is None:
        driver.close()
    else:
        print(len(facility_list))
# Facility URLs Dataframe
facility_table_urls = pd.DataFrame(facility_list)
facility_table_urls.to_excel("KMPDC_Facility_Details.xlsx")





    


