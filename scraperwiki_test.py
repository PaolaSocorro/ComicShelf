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



# import requests, bs4
# title = "Batman_Eternal"
# res = requests.get('https://en.wikipedia.org/wiki/'+title)
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'html.parser')
# elems = soup.select('.infobox')
# # print elems
# print type(elems)
# auth = soup.select()
# infoboxElem = elems[0]
# print infoboxElem
# infoboxElem.text
# infoboxElem.contents



import requests, bs4
res = requests.get('https://en.wikipedia.org/wiki/List_of_comics_publishing_companies')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')


table = soup.findAll('table')[1]

for row in table:
    text = str(row)
    r_soup = bs4.BeautifulSoup(text, 'html.parser')
    td = r_soup.findAll('td')
    # print row
    print td

# print table







