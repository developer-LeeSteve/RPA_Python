import requests

from bs4 import BeautifulSoup

# companyName 기업 이름
# companyPrice = 기업 주가
# companyPriceChange = 기업 주가 등락
# companyMCap = 기업 시가총액
# companyForeignPercentage = 주식 외인 보유 비중
# companyForeignSoldQuantity = 전일 외인 주식 순매매량
# sectorName = 업종
# sectorChange = 업종 등락비율

url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
base_url = 'https://finance.naver.com'

reqMain = requests.get(url)
html = reqMain.text
soup = BeautifulSoup(html, 'html.parser')

companyList = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')

tbCount = len(companyList)
companyCount = 0
cnt = 0

check = False
for i in range(tbCount):

	if i > 0:

		if cnt > 0:
			cnt -= 1
			continue

		companyName = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ') > td:nth-child(2) > a').get_text()

		if companyName == 'SK하이닉스':

			companyRow = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ')')

			companyPrice = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ') > td:nth-child(3)').get_text()

			companyPriceChange = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ') > td:nth-child(5) > span').get_text()
			companyPriceChange = companyPriceChange[5:-5]
			if len(companyPriceChange) == 0:
				companyPriceChange = str(0)
			elif companyPriceChange[0] != '-':
				companyPriceChange = '+' + companyPriceChange

			tempMCap = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ') > td:nth-child(7)').get_text()
			companyMCap = ''.join([x for x in tempMCap if x.isdigit()]) + '0'*8
			companyMCap = int(companyMCap)/((10)**12)
			companyMCap = "%.1f" %companyMCap

			companyForeignPercentage = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ') > td:nth-child(9)').get_text()

			companyLink = soup.select_one('#contentarea > div.box_type_l > table.type_2 > tbody > tr:nth-child(' + str(i+1) + ') > td:nth-child(2) > a', href=True)

			urlCompany = base_url + companyLink['href']
			reqCompany = requests.get(urlCompany)
			htmlCompany = reqCompany.text
			soupCompany = BeautifulSoup(htmlCompany, 'html.parser')

			check = True

			break

		companyCount += 1

		if companyCount%5 == 0:
			cnt += 3

		if i == tbCount-1 and check == False:
			print('해당 기업이 존재하지 않습니다.')

if check:
	# 외인 순매매량
	companyForeignSoldQuantity = soupCompany.select_one('#content > div.section.invest_trend > div.sub_section.right > table > tbody > tr:nth-child(2) > td:nth-child(4) > em').get_text()
	companyForeignSoldQuantity = int(''.join([x for x in companyForeignSoldQuantity[5:-5] if x.isdigit() or x=='-']))
	companyForeignSoldQuantity = "%.1f" %(companyForeignSoldQuantity/1000)

	# 업종 / 업종 등락
	sectorName = soupCompany.select_one('#content > div.section.trade_compare > h4 > em > a').get_text()
	sectorLink = soupCompany.select_one('#content > div.section.trade_compare > h4 > em > a', href=True)
	sectorUrl = base_url + sectorLink['href']

	reqSector = requests.get(sectorUrl)
	htmlSector = reqSector.text
	soupSector = BeautifulSoup(htmlSector, 'html.parser')

	sectorFind = soupSector.find('table', {'class':'type_1'})
	sectorTable = sectorFind.find_all("tr")[3]
	sectorChange = sectorTable.find_all("td")[1].get_text()
	sectorChange = sectorChange[6:-6]

	# 뉴스 기사 - 제목3개

	newsTitleList = []
	for i in range(5):
		companyNewsLink = soupCompany.select_one('#content > div.section.new_bbs > div.sub_section.news_section > ul:nth-child(2) > li:nth-child(' + str(i+1) + ') > span > a', href=True)
		newsUrl = base_url + companyNewsLink['href']

		reqNews = requests.get(newsUrl)
		htmlNews = reqNews.text
		soupNews = BeautifulSoup(htmlNews, 'html.parser')

		newsFind = soupNews.find('table', {'class':'view'})
		newsTitleTable = newsFind.find_all("tr")[0]
		companyNewsTitle = newsTitleTable.get_text()
		newsTitleList.append(companyNewsTitle)

	# print(newsUrl)
	# print('기업: ' + companyName)
	# print('주가: ' + companyPrice)
	# print('주가 등락: ' + companyPriceChange)
	# print('시가총액(조원): ' + companyMCap)
	# print('외인 보유 비중: ' + companyForeignPercentage + '%')
	# print('외인 순매매량(천): ' + companyForeignSoldQuantity)
	# print(str(sectorName) + '지수: ' + sectorChange)
	# print('증시동향:\n\t' + newsTitleList[0] + '\n\t' + newsTitleList[1] + '\n\t' + newsTitleList[2] + '\n\t' + newsTitleList[3] + '\n\t' + newsTitleList[4])

def main1():
	return companyName
def main2():
	return companyPrice
def main3():
	return companyPriceChange+'%'
def main4():
	return companyMCap
def main5():
	return companyForeignPercentage+'%'
def main6():
	return companyForeignSoldQuantity
def main7():
	return sectorName
def main8():
	return sectorChange
def main9():
	return newsTitleList[0]
def main10():
	return newsTitleList[1]
def main11():
	return newsTitleList[2]
def main12():
	return newsTitleList[3]
def main13():
	return newsTitleList[4]