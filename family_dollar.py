from requests import get# for making standard html requests
from bs4 import BeautifulSoup as bs # magical tool for parsing html data
import json # for parsing data
from pandas import DataFrame as df # premier library for data organization

url = 'https://locations.familydollar.com/id/'

page = get(url)
soup = bs(page.content, 'html.parser')

arco = soup.find_all(type="application/ld+json")

city_hrefs = [] # initialise empty list
dollar_tree_list = soup.find_all(class_='itemlist')
for i in dollar_tree_list:
    cont = i.contents[0]
    href = cont['href']
    city_hrefs.append(href)

page2 = get(city_hrefs[2]) # again establish a representative example
soup2 = bs(page2.text, 'html.parser')

arco = soup2.find_all(type="application/ld+json")

arco_contents = arco[1].contents[0]

arco_json =  json.loads(arco_contents)

arco_address = arco_json['address']

locs_dict = [] # initialise empty list

for link in city_hrefs:
    locpage = get(link)   # request page info
    locsoup = bs(locpage.text, 'html.parser')
      # parse the page's content
    locinfo = locsoup.find_all(type="application/ld+json")
      # extract specific element
    loccont = locinfo[1].contents[0]
      # get contents from the bs4 element set
    locjson = json.loads(loccont)  # convert to json
    locaddr = locjson['address'] # get address
    locs_dict.append(locaddr) # add address to list

locs_df = df.from_records(locs_dict)
locs_df.drop(['@type', 'addressCountry'], axis=1, inplace=True)
locs_df.head(n=5)
df.to_csv(locs_df, "family_dollar_ID_locations.csv", sep = ",", index = False)
