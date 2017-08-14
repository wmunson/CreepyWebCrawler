
import csv
import requests
import re
# from selenium import webdriver
from bs4 import BeautifulSoup as bs
from models import RowMatch, Fund, Holding

def inital_req():

	cik_test = "0001166559"
	date_test = ""
	type_test = "13F"
	count_test = "10000"

	url_start = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+cik_test+"&Stype="+type_test+"&dateb="+date_test+"&owner=exclude&count="+count_test
# Inital request ###########
		
	match_row_list =[]

	try:
		req = requests.get(url_start)
		return doc = bs(req.text, "html.parser")
	except RequestError:
		return "There was an error with that request."
def get_fund_name(doc):

	comp_div = doc.find_all("span")
	print(len(comp_div))
	for span in comp_div:
		name_match = re.search(r'\sclass="companyName">',span.decode())
		if name_match:
			info_match = re.match(r'^(.)+\sCIK#:\s(\d)+',span.text)
			info = info_match.group()
			info = re.split(r'\sCIK#:\s',info)
			fund = Fund(name = info[0], cik=info[1],list_of_holdings=[])

# print(fund)
# print(comp_div)
	table = doc.find_all(summary="Results")
# print(len(table))

	row_list = table[0].find_all('tr')
# print(type(tr))
# print(dir(doc))
# print(tr_list)
for row in row_list[1:]:  #Skipping header row which is empty
	td = row.find_all('td')
	# print(len(td))
	file_type = td[0].text
	# print(file_type)
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
# print(dir(row[0]))
# print(len(row_list))
# print(match_row_list[0])
# print(len(match_row_list))



## Second(inner) request ####
''
inner_req = requests.get(match_row_list[10].file_link)
in_doc = bs(inner_req.text, "html.parser")
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==========')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==============================')
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# print("https://www.sec.gov"+match_row_list[0].file_link)

# print(in_doc)
in_table = in_doc.find_all(summary="Document Format Files")

# print(in_table[0])
in_row_list = in_table[0].find_all('tr')
''
for in_row in in_row_list[1:]:
	in_td = in_row.find_all('td')
	# print(in_td[0]) 
	# print(in_td[1].text)
	info_text =  in_td[3].text
	# print('yaaa', re.match('INFORMATION TABLE', info_text))
	info_check = re.match('INFORMATION TABLE', info_text)
	# print(in_td[2].text)
	# print(in_td[2].select('a')[0]['href'])
	file_href = in_td[2].select('a')[0]['href']
	xml_text = in_td[2].text
	# print("good",re.search(r'.xml$', xml_text))
	xml_check = re.search(r'.xml$', xml_text) 
	# print(in_td[3]) 
	# print(in_td[4]) 
	# print('========')
	if info_check != None and xml_check != None:
		file_req = requests.get("https://www.sec.gov"+file_href)
		# print(file_req.text)
		holding_doc = bs(file_req.text, "html.parser")
		print(holding_doc)
		info_tabels = holding_doc.find_all("infotable")
		# print(info_tabels)
		print(len(info_tabels))
		# print(info_tabels[0],'\n')
		# print(info_tabels[1],'\n')
		# print(info_tabels[2],'\n')
		# print(info_tabels[3],'\n')
		# print(info_tabels[4],'\n')
		# print(info_tabels[5],'\n')
		# print(info_tabels[6],'\n')
		# print(info_tabels[7],'\n')
		# print(info_tabels[8],'\n')
		# print(info_tabels[9],'\n')
		# print(info_tabels[10],'\n')
		# print(info_tabels[11],'\n')
		# print(info_tabels[12],'\n')
		# print(info_tabels[13],'\n')
		# print(info_tabels[14],'\n')
		# print(info_tabels[15],'\n')
		# print(info_tabels[16],'\n')
		# print(info_tabels[17],'\n')
		# print(info_tabels[18].findChild('nameofissuer'))
		for comp in info_tabels:
			# print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
			name_of_issuer = comp.findChild('nameofissuer')
			# print('name:',name_of_issuer.text)
			title_of_class = comp.findChild('titleofclass')
			# print('title:', title_of_class.text)
			cusip = comp.findChild('cusip')
			# print('cusip:', cusip.text)
			value = comp.findChild('value')
			# print('value:', value.text)

			shr = comp.findChild('shrsorprnamt')
			# print('shr:', shr.text)
			prn_amt_prn = shr.findChild('sshprnamt')
			# print('prnamt:', prn_amt_prn.text)
			shr_or_sh = shr.findChild('sshprnamttype')
			# print('shr or sh: ', shr_or_sh.text)

			put_call = comp.findChild('nameofissuer')
			# print('putcall:', put_call.text)
			investment_discretion = comp.findChild('investmentdiscretion')
			# print('discretion:', investment_discretion.text)
			other_manager = comp.findChild('nameofissuer')
			# print('man:', other_manager.text)
			
			voting = comp.findChild('votingauthority')
			# print('voting:', voting.text)
			sole_voting_auth = voting.findChild('sole')
			# print('sole:', sole_voting_auth.text)
			shared_voting_auth = voting.findChild('shared')
			# print('shared:',shared_voting_auth.text)
			no_voting_auth = voting.findChild('none')
			# print('none:', type(no_voting_auth.text))
			# print(match_row_list[10].date)
			holding=Holding(date=match_row_list[10].date,
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
			fund.list_of_holdings.append(holding)

print(fund)
print(len(fund.list_of_holdings))
print(holding.writing_list)
fund.write_file()

with open("BILL & MELINDA GATES FOUNDATION TRUST, 2014-11-14", 'r') as file:
	file.readlines()