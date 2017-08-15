
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
		self.writing_list = [self.name_of_issuer, self.title_of_class, 
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

		### Perfroms the writing to new files based on Fund name and each filing date
	def write_file(self):
		print('len of holding list', len(self.list_of_holdings))
		
		for holding in self.list_of_holdings:
			print(holding.date)
			file = open("results/"+self.name+", "+holding.date,"a")
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
