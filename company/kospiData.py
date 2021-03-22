import requests

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

kospi = soup.select_one('#KOSPI_now').get_text()
tempkospiChange = soup.select_one('#KOSPI_change').get_text()

kospiChange = ''
check = False

for i in tempkospiChange:
	if check:
		kospiChange += i
	if i == ' ':
		check = True
	if i == '%':
		check = False

def main1():
	return kospi
def main2():
	return kospiChange