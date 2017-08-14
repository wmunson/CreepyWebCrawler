from bs4 import BeautifulSoup as bs
import requests
import re

class Holding:

	def __init__(self,
				date, 
				name_of_issuer, title_of_class, 
				cusip, value, shr_or_sh, prn_amt_prn, 
				put_call, investment_discretion, 
				other_manager, sole_voting_auth, 
				shared_voting_auth, no_voting_auth
				):
		self.date = date
		self.name_of_issuer = name_of_issuer
		self.title_of_class = title_of_class
		self.cusip = cusip
		self.value = value
		self.prn_amt_prn = prn_amt_prn
		self.shr_or_sh = shr_or_sh
		self.put_call = put_call
		self.investment_discretion = investment_discretion
		self.other_manager = other_manager
		self.sole_voting_auth = sole_voting_auth
		self.shared_voting_auth = shared_voting_auth
		self.no_voting_auth = no_voting_auth
		self.writing_list = [self.date, self.name_of_issuer, self.title_of_class, 
				self.cusip, self.value, self.shr_or_sh, self.prn_amt_prn, 
				self.put_call, self.investment_discretion, 
				self.other_manager, self.sole_voting_auth, 
				self.shared_voting_auth, self.no_voting_auth]

	def __str__(self):
		return self.name_of_issuer


class Fund:

	def __init__(self, name, cik, list_of_holdings):
		self.name = name
		self.cik = cik
		self.list_of_holdings = list_of_holdings

	def __str__(self):
		return self.name


	def write_file(self):
		
		print('len of holding list', len(self.list_of_holdings))
		for holding in self.list_of_holdings:
			# print(holding)
			with open(self.name+", "+holding.date,"a") as file:
					file.write(("\t").join(holding.writing_list) + "\n")
			file.close()
				

class RowMatch:

	def __init__(self, file_type, file_link, date, details):
		self.file_type = file_type
		self.file_link = "https://www.sec.gov"+file_link
		self.date = date
		self.details = details

	def __str__(self):
		return self.date+" "+self.details

	def file_request(self):
		
		inner_req = requests.get(match_row_list[10].file_link)
		in_doc = bs(inner_req.text, "html.parser")
		in_table = in_doc.find_all(summary="Document Format Files")
		in_row_list = in_table[0].find_all('tr')

		for in_row in in_row_list[1:]: ### skips header row
			in_td = in_row.find_all('td')
			info_text =  in_td[3].text
			info_check = re.match('INFORMATION TABLE', info_text)
			file_href = in_td[2].select('a')[0]['href']
			xml_text = in_td[2].text
			xml_check = re.search(r'.xml$', xml_text)
			
			if info_check != None and xml_check != None:
				file_req = requests.get("https://www.sec.gov"+file_href)
				holding_doc = bs(file_req.text, "html.parser")
				info_tabels = holding_doc.find_all("infotable")

		return info_tabels