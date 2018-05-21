import urllib.request
from bs4 import BeautifulSoup

# 네이버 웹툰 > 마음의 소리
# data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fn')
# soup = BeautifulSoup(data, 'html5lib')
# # print(soup)
# cartoons = soup.findAll('td', attrs = {'class':'title'})
# for item in cartoons:
#     title = item.find('a').text
#     print(title)

# TED Talks > 한국어
data = urllib.request.urlopen('https://www.ted.com/talks?sort=newest&language=ko')
soup = BeautifulSoup(data, 'lxml')
talkVideos = soup.findAll('div', attrs={'class':'media__message'})
html='<html><head></head><body>'
for item in talkVideos:
    title = item.find('a', attrs={'class':' ga-link'}).text
    link = item.find('a')['href']
    # print('{}<br />', title)
    # print('<a href=ted.com{}>{}</a>', link, title)
    html += '<a href=\'http://ted.com'+link+'\'>'+title+'</a><br />'
    # print(title.strip())
    # print(link.strip())
html+='</body></html'

outputSoup = BeautifulSoup(html)
metaTag = outputSoup.new_tag('meta')
metaTag.attrs['charset'] = 'utf-8'
outputSoup.head.append(metaTag)
html5 = str(outputSoup.prettify())
f = open('TED Talks.html', 'w')
f.write(html5)
f.close()
