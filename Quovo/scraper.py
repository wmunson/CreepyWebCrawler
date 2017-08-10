import sys
import csv
import requests

from bs4 import BeautifulSoup as bs

url_start = "http://www.sec.gov/edgar/searchedgar/companysearch.html"

cil_test = "0001166559"

req = requests.get(url_start)

doc = bs(req.text, "html.parser")
print('===========================================================================================')
print('========================================================================================================')
print('===============================================================================================')
print('=================================================================')
print(doc.head)