# import requests,bs4

# title = "Batman_Eternal"
# url = 'http://en.wikipedia.org/wiki/' + title

# response = requests.get(url, params={'action':'raw'})
# page = response.text

# response.raise_for_status()

# soup = bs4.BeautifulSoup(response.text,'html.parser')


# soup.select('#toc')
# infoboxElem = elems[0]
# infoboxElem.text
# infoboxElem.contents

# "metadata plainlinks ambox ambox-style ambox-lead_too_short" 

### look into beautiful soup parsers

import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
title = "Batman_Eternal"
url = "https://en.wikipedia.org/wiki/"+title
# res = requests.get('https://en.wikipedia.org/wiki/'+title)
html = urlopen(url)
wikiobj = BeautifulSoup(html, "html.parser")
char_table = wikiobj.find("div",{"id":"mw-content-text"})

info_t = char_table.table.next_sibling

print info_t
# new_info = info_t.find("table",{"class":"infobox"})
# print new_info
# print char_table
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'html.parser') # get html from requests, and html5lib
# elems = soup.find('.infobox')
# print elems
# print type(elems)
# auth = soup.select()
# infoboxElem = elems[0]
# print infoboxElem
# infoboxElem.text
# infoboxElem.contents



# import requests, bs4
# res = requests.get('https://en.wikipedia.org/wiki/List_of_comics_publishing_companies')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'html.parser')


# table = soup.findAll('table')[1]
# print table


# for row in table:
#     text = str(row)
#     r_soup = bs4.BeautifulSoup(text, 'html.parser')
#     td = r_soup.findAll('td')
#     # print row
#     # print td

# print table







