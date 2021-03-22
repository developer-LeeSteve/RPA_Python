import requests

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

companyName1 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(2) > a').get_text()
companyPrice1 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(3)').get_text()
comapnyPriceChange1 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(2) > td:nth-child(5) > span').get_text()[5:-5]

companyName2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3) > td:nth-child(2) > a').get_text()
companyPrice2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3) > td:nth-child(3)').get_text()
comapnyPriceChange2 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(3) > td:nth-child(5) > span').get_text()[5:-5]

companyName3 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(4) > td:nth-child(2) > a').get_text()
companyPrice3 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(4) > td:nth-child(3)').get_text()
comapnyPriceChange3 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(4) > td:nth-child(5) > span').get_text()[5:-5]

companyName4 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(5) > td:nth-child(2) > a').get_text()
companyPrice4 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(5) > td:nth-child(3)').get_text()
comapnyPriceChange4 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(5) > td:nth-child(5) > span').get_text()[5:-5]

companyName5 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(6) > td:nth-child(2) > a').get_text()
companyPrice5 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(6) > td:nth-child(3)').get_text()
comapnyPriceChange5 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(6) > td:nth-child(5) > span').get_text()[5:-5]

companyName6 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(10) > td:nth-child(2) > a').get_text()
companyPrice6 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(10) > td:nth-child(3)').get_text()
comapnyPriceChange6 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(10) > td:nth-child(5) > span').get_text()[5:-5]

companyName7 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(11) > td:nth-child(2) > a').get_text()
companyPrice7 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(11) > td:nth-child(3)').get_text()
comapnyPriceChange7 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(11) > td:nth-child(5) > span').get_text()[5:-5]

companyName8 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(12) > td:nth-child(2) > a').get_text()
companyPrice8 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(12) > td:nth-child(3)').get_text()
comapnyPriceChange8 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(12) > td:nth-child(5) > span').get_text()[5:-5]

companyName9 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(13) > td:nth-child(2) > a').get_text()
companyPrice9 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(13) > td:nth-child(3)').get_text()
comapnyPriceChange9 = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(13) > td:nth-child(5) > span').get_text()[5:-5]