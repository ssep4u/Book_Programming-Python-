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
soup = BeautifulSoup(data, 'html5lib')
talkVideos = soup.findAll('div', attrs={'class':'media__message'})
for item in talkVideos:
    title = item.find('a', attrs={'class':' ga-link'}).text
    print(title.strip())
