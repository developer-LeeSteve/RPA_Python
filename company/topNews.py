import requests

from bs4 import BeautifulSoup

url = 'https://finance.naver.com/news/mainnews.nhn'

req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

mainNewsTitle = soup.select_one('#contentarea_left > div.mainNewsList > ul > li:nth-child(1) > dl > dd.articleSubject > a').get_text()
mainNewsContent = soup.select_one('#contentarea_left > div.mainNewsList > ul > li:nth-child(1) > dl > dd.articleSummary').get_text()[11:]

dotCnt = 0
for i in range(len(mainNewsContent)):
	if mainNewsContent[i] == '.':
		dotCnt += 1
	if dotCnt == 2:
		mainNewsContent = mainNewsContent[:i+1]
		break

print('기사 제목: ' + mainNewsTitle)
print('기사 내용: ' + mainNewsContent)