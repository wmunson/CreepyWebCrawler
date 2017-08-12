import sys
import csv
import requests
import re
# from selenium import webdriver
from bs4 import BeautifulSoup as bs

cik_test = "0001166559"
date_test = ""
type_test = ""
count_test = "10000"

# chrome = webdriver.Chrome(executable_path="chromedriver.exe")

url_start = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+cik_test+"&Stype="+type_test+"&dateb="+date_test+"&owner=exclude&count="+count_test
url2 = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&type=&dateb=&owner=exclude&count=100'	
		
# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&owner=exclude&count=40
# https://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&owner=exclude&action=getcompany
# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&type=&dateb=&owner=exclude&count=100
# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001166559&type=&dateb=&owner=exclude&count=10000
# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+cik_test+"type="+type_test+"&dateb="+date_test+"&owner=exclude&count="+count_test

req = requests.get(url_start)
# ch = chrome.get(url_start)
# print(ch)
doc = bs(req.text, "html.parser")
print('===========================================================================================')
print('========================================================================================================')
print('===============================================================================================')
print('=================================================================')
print(dir(doc))
table = doc.find_all(summary="Results")
print(len(table))

for row in table.find_all("tr")[1:]:  # skipping header row
    cells = row.find_all("td")
    print(cells[0].text, cells[1].find('a').text)




# tr_list = table[0].find_all('tr')
# # print(type(tr))
# # print(dir(doc))
# # print(tr_list)
# for tr in tr_list:
# 	td = tr.find_all('td')
# 	print(len(td))
# 	# print(len(tr))
# 	# print(tr)
# 	print(dir(td))
# 	print(td.index('href'))
# 	# for item in td:
# 		# print(len(item))
# # print(dir(tr[0]))
# print(len(tr_list))