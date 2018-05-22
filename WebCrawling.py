from urllib.request import urlopen
from bs4 import BeautifulSoup

# 네이버 웹툰 > 마음의 소리
# data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fn')
# soup = BeautifulSoup(data, 'html5lib')
# soup = BeautifulSoup(data, 'lxml')
# # print(soup)
# cartoons = soup.findAll('td', attrs = {'class':'title'})
# for item in cartoons:
#     title = item.find('a').text
#     print(title)

# TED Talks > 한국어
# 웹사이트 접속해서 html 가져오기
html = urlopen('https://www.ted.com/talks?sort=newest&language=ko')
data = html.read()
html.close()

# 구조 파악해서 필요한 부분만 추출하기
# 추출한 정보로 새로운 html 만들기
soup = BeautifulSoup(data, 'lxml')
talkVideos = soup.findAll('div', attrs={'class':'media__message'})
htmlOutput='<html><head></head><body>'
for item in talkVideos:
    title = item.find('a', attrs={'class':' ga-link'}).text
    link = item.find('a')['href']
    # print(title.strip())
    # print(link.strip())
    htmlOutput += '<a href=\'http://ted.com'+link+'\'>'+title+'</a><br />'
htmlOutput+='</body></html>'

# 한글 보이도록 encoding 정보 넣기
# 파일로 출력하기
outputSoup = BeautifulSoup(htmlOutput, 'lxml')
metaTag = outputSoup.new_tag('meta')
metaTag.attrs['charset'] = 'utf-8'
outputSoup.head.append(metaTag)
html5 = str(outputSoup.prettify())
f = open('TED Talks.html', 'w')
f.write(html5)
f.close()
