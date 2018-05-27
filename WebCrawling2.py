from urllib.request import urlopen
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
data = urlopen('https://www.ted.com/talks?sort=newest&language=ko')
soup = BeautifulSoup(data, 'lxml')
talkVideos = soup.find_all('div', attrs={'class':'media__message'})
html='<html><head><meta charset=\'utf-8\' /></head><body>'
for item in talkVideos:
    title = item.find('a', attrs={'data-ga-context':'talks'}).text
    link = item.find('a').get('href')
    # print('{}<br />'.format(title))
    html += '<a href=\'http://ted.com'+link+'\'>'+title+'</a><br />'
    # print('<a href=ted.com{}>{}</a>'.format(link, title)
    # print(title.strip())
    # print(link.strip())
html+='</body></html>'

outputSoup = BeautifulSoup(html, 'lxml')
# metaTag = outputSoup.new_tag('meta')
# metaTag.attrs['charset'] = 'utf-8'
# outputSoup.head.append(metaTag)
resultHtml = str(outputSoup.prettify()).encode('utf-8')
# print(resultHtml)
f = open('TED Talks.html', 'wb')
f.write(resultHtml)
f.close()
