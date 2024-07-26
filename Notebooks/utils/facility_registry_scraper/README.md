# KMPDB-Facility-Register-Scraper
Scarpe registered facilities from the KMPDU [website](http://kmpdc.go.ke/Registers/H-Facilities.php) and determine their locations through the Google Maps API.

## Tools
- BeautifulSoup
- Selenium with WebDrvier using Chrome

If using WSL in windows be sure to install Chrome browser
```bash
$: cd /tmp
$: sudo dpkg -i google-chrome-stable_current_amd64.deb
$: sudo apt install --fix-broken -y
```

## Steps
1. Create a shell environment using ```pipenv shell```
2. Install packages using the requirements.txt file within your own shell environment using ```pipenv install -r requirements.txt```.
3. Run ```facility_scraper.py``` to download the registered list of facilities on the board registry and their respective urls.
4. Run ```facility_url.py``` to download the further details of registered facilites.
> NOTE: the url list has empty cells at the top of the excel file once ```facility_scraper.py``` finishes running. Remember to remove empty cell. Also mark the column with the urls with the tag ```View``` before running ```facility_url.py```.
