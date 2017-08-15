from tools import make_parse_req, check_req_results, inital_req, get_fund_name, match_rows, file_request, make_holdings_list
from models import Fund

def main():
	start_search()


def start_search():
	search_results = inital_req()
	# print(search_results)
	check_req_results(search_results)
	# print(type(search_results))
	fund_info = get_fund_name(search_results)
	matched_files_list = match_rows(search_results)
	# print('file list',matched_files_list)
	match_files_req(matched_files_list, fund_info)
	


def match_files_req(row_list, fund_info):
	print('row list',len(row_list))
	
	for row in row_list:
		tables, date = file_request(row)
		# print('tables',tables)
		holdings_list = (make_holdings_list(tables, date))
		# print('holding OUT', holdings_list)
		fund = Fund(name=fund_info[0], cik=fund_info[1], list_of_holdings=holdings_list)
		# print('fund list',fund.list_of_holdings)
		fund.write_file()
	return "Complete"



if __name__ == '__main__':
	main()