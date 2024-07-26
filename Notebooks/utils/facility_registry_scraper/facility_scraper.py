import logging
import requests, re
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

browser = webdriver.Chrome()

url = "http://kmpdc.go.ke/Registers/H-Facilities.php"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"})

soup = BeautifulSoup(response.content, "html.parser")

facility_list = []
# Get Facility Details in all tables
facility_rows = soup.find_all("tr")
for row in facility_rows:
    facility = row.get_text("td")
    # regex to replace 'td' string as empty string
    new_string = re.sub(r'td', "", facility)
    facility_list.append(new_string.split('\n'))

# Facility Table Dataframe
facility_table = pd.DataFrame(facility_list)
facility_table.to_excel("KMPDC_Registered_Facilites.xlsx")

facility_urls = []
# Get all Facility Urls
href = soup.find_all("a")
for urls in href:
    base_url = urls.get('href')
    url = 'http://kmpdc.go.ke/Registers/'+ base_url
    facility_urls.append(url)

# Facility URLs Dataframe
facility_table_urls = pd.DataFrame(facility_urls)
facility_table_urls.to_excel("KMPDC_Facility_URLs.xlsx")

# Merge Dataframes - requires editing number of aligned rows for the urls
facility_registry = pd.concat([facility_table,facility_table_urls],axis=1)
facility_registry.to_excel("KMPDC_Facility_Registry.xlsx")