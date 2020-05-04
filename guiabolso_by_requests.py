from requests import get, post
import json
from pprint import pprint

headers = {
    'authority': 'www.guiabolso.com.br',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://www.guiabolso.com.br',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.guiabolso.com.br/web/',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'visid_incap_151208=OvFK2i/0Q7yzG7VKYa6/juJIo14AAAAAQUIPAAAAAAA0g/IyZH8r7iSKxrOKz3Jk; nlbi_151208=Jbm+SGZetx7iz+l+mdUmqAAAAAC0CvkW0Z8LSlRlfFhMnmD4; incap_ses_685_151208=4GSVYVxbmkrtqMKR45uBCQ9Jo14AAAAAjBqM86WoejJL80fkqZrs8w==; _ga=GA1.3.176915099.1587759382; _gid=GA1.3.1591339431.1587759382; _gat_UA-33448985-2=1; _gat_UA-33448985-1=1',
}

data = '{"name":"web:users:login","version":"1",
"payload":{
    "email":"zicadopv@gmail.com",
    "pwd":"luxu1650",
    "userPlatform":"GUIABOLSO","deviceToken":"009a8d19d966295d7bb431ba092c6cf0","os":"Windows","appToken":"1.1.0","deviceName":"009a8d19d966295d7bb431ba092c6cf0"},"flowId":"14c11cfb-e819-4b90-84de-309ddeb022dc","id":"b7977fc6-12ed-494e-b8cb-198c11138763","auth":{"token":null,"x-sid":"d39d8917-3516-406f-8f37-25221f43f127","x-tid":"049373a8-b6b6-4430-8fb2-6e87324ce898"},"metadata":{"origin":"web","appVersion":"1.0.0","createdAt":"2020-04-24T20:30:09.100Z"},"identity":{}}'

url = 'https://www.guiabolso.com.br/comparador/v2/events/others'

response = post(
    url, 
    headers=headers, 
    data=data
)

pprint(json.loads(response.text))
