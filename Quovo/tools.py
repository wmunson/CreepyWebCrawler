import requests
import re
# from selenium import webdriver
from bs4 import BeautifulSoup as bs
from models import RowMatch, Holding


## Handels Get Requests and Beautiful Soup Parsing ##
def make_parse_req(url):
	try:
		req = requests.get(url)
		return bs(req.text, "html.parser")
	except:
		raise Exception("There was an error with that request.")

def check_req_results(req):
	bad_cik_pattern = re.compile('No matching CIK.')
	bad_url_pattern = re.compile("Oops! We can't find this file")
	
	if bad_cik_pattern.search(req.decode()):
		raise Exception("CIK returned no results.")
	elif bad_url_pattern.search(req.decode()):
		raise Exception("URL returned no results.")
	else:
		pass 


## Takes user input and can handle customized searches 
def inital_req():
	cik_input = input('Welcome! Please enter a CIK or Ticker. \nThe result of your search will be the "results" folder: ')

	# 0001632554  #Trust Co
	# 0001166559  #BMGF

	cik_test = "0001166559"
	date_test = ""
	type_test = ""
	count_test = "10000"

	url_start = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+cik_test+"&Stype="+type_test+"&dateb="+date_test+"&owner=exclude&count="+count_test
	print(url_start)
	return make_parse_req(url_start)

## Gets fund name for making txt files ###
def get_fund_name(doc):

	comp_div = doc.find_all("span")
	# print(len(comp_div))
	for span in comp_div:
		name_match = re.search(r'\sclass="companyName">',span.decode())
		print(name_match)
		if name_match:
			info_match = re.match(r'^(.)+\sCIK#:\s(\d)+',span.text)
			
			info = info_match.group()    #### Contains the name @ info[0] and CIK @ info[1]
			return re.split(r'\sCIK#:\s',info)
		

### Currently searching for "13F" file types and creating RowMatch objs
def match_rows(doc):
	
	match_row_list =[]
	table = doc.find_all(summary="Results")
	row_list = table[0].find_all('tr')

	for row in row_list[1:]:  #Skipping header row which is empty
		td = row.find_all('td')
		file_type = td[0].text
		type_check = re.match(r"13F",file_type)
		
		if type_check != None:
			# print(td[0].text)
			href = td[1].select('a')[0]['href']
			detail = td[2].text
			date = td[3].text 
			# print(href)
			# print(detail)
			# print(date)
			match_row_list.append(RowMatch(file_type=str(file_type),
											file_link=str(href),
											date=str(date),
											details=str(detail)))
	return match_row_list



## Parses inner page of each holding claim by date and returns xml file
def file_request(matched_row):
	
	doc = make_parse_req(matched_row.file_link)
	single_file_info_tabels=''
	in_table = doc.find_all(summary="Document Format Files")
	in_row_list = in_table[0].find_all('tr')

	for in_row in in_row_list[1:]: ### skips header row
		in_td = in_row.find_all('td')
		info_text =  in_td[3].text
		info_check = re.match('INFORMATION TABLE', info_text)
		file_href = in_td[2].select('a')[0]['href']
		xml_text = in_td[2].text
		xml_check = re.search(r'.xml$', xml_text)
		
		if info_check != None and xml_check != None:
			print('XML FOUND')

			holding_doc = make_parse_req("https://www.sec.gov"+file_href)
			# print(holding_doc)
			single_file_info_tabels = holding_doc.find_all(re.compile('infotable'))
 
	return single_file_info_tabels, matched_row.date



### Converts xml table of companies into Holding objs so information can be easily edited
def make_holdings_list(comp_list, date): ## takes in info_tables returned from def file_request
	holdings_list=[]
	for comp in comp_list:

		name_of_issuer = comp.findChild(re.compile('nameofissuer'))
		title_of_class = comp.findChild(re.compile('titleofclass'))
		cusip = comp.findChild(re.compile('cusip'))
		value = comp.findChild(re.compile('value'))
		shr = comp.findChild(re.compile('shrsorprnamt'))
		
		prn_amt_prn = shr.findChild(re.compile('sshprnamt'))
		shr_or_sh = shr.findChild(re.compile('sshprnamttype'))

		put_call = comp.findChild(re.compile('nameofissuer'))
		investment_discretion = comp.findChild(re.compile('investmentdiscretion'))
		other_manager = comp.findChild(re.compile('nameofissuer'))
		
		voting = comp.findChild(re.compile('votingauthority'))
		sole_voting_auth = voting.findChild(re.compile('sole'))
		shared_voting_auth = voting.findChild(re.compile('shared'))
		no_voting_auth = voting.findChild(re.compile('none'))
	
		holding=Holding(date=date,
				name_of_issuer=name_of_issuer.text,
				title_of_class=title_of_class.text,
				cusip=cusip.text,
				value=value.text,
				prn_amt_prn=prn_amt_prn.text,
				shr_or_sh=shr_or_sh.text,
				put_call=put_call.text,
				investment_discretion=investment_discretion.text,
				other_manager=other_manager.text,
				sole_voting_auth=sole_voting_auth.text,
				shared_voting_auth=shared_voting_auth.text,
				no_voting_auth=no_voting_auth.text
				)
		holdings_list.append(holding)
	
	return holdings_list

