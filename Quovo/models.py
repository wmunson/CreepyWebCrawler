

class Holding:

	def __init__(self, 
				name_of_issuer, title_of_class, 
				cusip, value, shr_or_sh_or_prn_amt_prn, 
				put_call, investment_discretion, 
				other_manager, sole_voting_auth, 
				shared_voting_auth, no_voting_auth
				):
		self.name_of_issuer = name_of_issuer
		self.title_of_class = title_of_class
		self.cusip = cusip
		self.value = value
		self.shr_or_sh_or_prn_amt_prn = shr_or_sh_or_prn_amt_prn
		self.put_call = put_call
		self.investment_discretion = investment_discretion
		self.other_manager = other_manager
		self.sole_voting_auth = sole_voting_auth
		self.shared_voting_auth = shared_voting_auth
		self.no_voting_auth = no_voting_auth

	def __str__(self):
		return self.name_of_issuer


class Fund:

	def __intit__(self, name, year, list_holdings):
		self.name = name
		self.year = year
		self.list_holdings = list_holdings

class RowMatch:

	def __init__(self, file_type, file_link, date, details):
		self.file_type = file_type
		self.file_link = file_link
		self.date = date
		self.details = details

	def __str__(self):
		return self.description, self.date