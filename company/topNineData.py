import requests

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

companyName1 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a').get_text()
companyPrice1 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(3)').get_text()
companyPriceChange1 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(5) > span').get_text()[5:-5]

companyName2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3) > td:nth-child(2) > a').get_text()
companyPrice2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3) > td:nth-child(3)').get_text()
companyPriceChange2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3) > td:nth-child(5) > span').get_text()[5:-5]

companyName3 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(4) > td:nth-child(2) > a').get_text()
companyPrice3 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(4) > td:nth-child(3)').get_text()
companyPriceChange3 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(4) > td:nth-child(5) > span').get_text()[5:-5]

companyName4 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(5) > td:nth-child(2) > a').get_text()
companyPrice4 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(5) > td:nth-child(3)').get_text()
companyPriceChange4 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(5) > td:nth-child(5) > span').get_text()[5:-5]

companyName5 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(6) > td:nth-child(2) > a').get_text()
companyPrice5 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(6) > td:nth-child(3)').get_text()
companyPriceChange5 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(6) > td:nth-child(5) > span').get_text()[5:-5]

companyName6 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(10) > td:nth-child(2) > a').get_text()
companyPrice6 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(10) > td:nth-child(3)').get_text()
companyPriceChange6 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(10) > td:nth-child(5) > span').get_text()[5:-5]

companyName7 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(11) > td:nth-child(2) > a').get_text()
companyPrice7 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(11) > td:nth-child(3)').get_text()
companyPriceChange7 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(11) > td:nth-child(5) > span').get_text()[5:-5]

companyName8 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(12) > td:nth-child(2) > a').get_text()
companyPrice8 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(12) > td:nth-child(3)').get_text()
companyPriceChange8 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(12) > td:nth-child(5) > span').get_text()[5:-5]

companyName9 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(13) > td:nth-child(2) > a').get_text()
companyPrice9 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(13) > td:nth-child(3)').get_text()
companyPriceChange9 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(13) > td:nth-child(5) > span').get_text()[5:-5]

def fcompanyName1():
	return companyName1
def fcompanyName2():
	return companyName2
def fcompanyName3():
	return companyName3
def fcompanyName4():
	return companyName4
def fcompanyName5():
	return companyName5
def fcompanyName6():
	return companyName6
def fcompanyName7():
	return companyName7
def fcompanyName8():
	return companyName8
def fcompanyName9():
	return companyName9

def fcompanyPrice1():
	return companyPrice1
def fcompanyPrice2():
	return companyPrice2
def fcompanyPrice3():
	return companyPrice3
def fcompanyPrice4():
	return companyPrice4
def fcompanyPrice5():
	return companyPrice5
def fcompanyPrice6():
	return companyPrice6
def fcompanyPrice7():
	return companyPrice7
def fcompanyPrice8():
	return companyPrice8
def fcompanyPrice9():
	return companyPrice9

def fcompanyPriceChange1():
	return companyPriceChange1
def fcompanyPriceChange2():
	return companyPriceChange2
def fcompanyPriceChange3():
	return companyPriceChange3
def fcompanyPriceChange4():
	return companyPriceChange4
def fcompanyPriceChange5():
	return companyPriceChange5
def fcompanyPriceChange6():
	return companyPriceChange6
def fcompanyPriceChange7():
	return companyPriceChange7
def fcompanyPriceChange8():
	return companyPriceChange8
def fcompanyPriceChange9():
	return companyPriceChange9
