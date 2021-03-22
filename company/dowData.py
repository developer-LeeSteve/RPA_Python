import requests

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/world/sise.nhn?symbol=DJI@DJI'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

dow = soup.select_one('#dayTable > tbody > tr:nth-child(1) > td.tb_td2 > span').get_text()
strDowBefore = soup.select_one('#dayTable > tbody > tr:nth-child(1) > td.tb_td4 > span').get_text()

floatDow = ''
floatDowBefore = ''
strChangeDow = ''

for i in dow:
	if i != ',':
		floatDow += i

for i in strDowBefore:
	if i != ',':
		floatDowBefore += i

strChangeDow += "%.2f" %((float(floatDow)-float(floatDowBefore)))
dowChange = "%.2f" %((float(strChangeDow)/float(floatDow))*100)
dowChange += '%'

def main1():
	return dow
def main2():
	return dowChange