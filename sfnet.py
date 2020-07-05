import lxml.html
from requests import get

url = 'https://www.sfnet.com/detail-pages/member-directory-company-profile-detail/addleshaw-goddard-llp-0fa9c5e6-d6b9-4956-8ae0-cd3e521823d0'

response = get(url)

html = lxml.html.fromstring(response.text)
soup = html.xpath('//*[@id="ContentPlaceholder_T8D6417F5001_Col02"]/div/p[1]/span[1]/br[1]')
soup2 = html.xpath('//*[@id="ContentPlaceholder_T8D6417F5001_Col02"]/div/p[1]/span[1]/br[2]')

print(soup[0].tail)
print(soup2[0].tail)
