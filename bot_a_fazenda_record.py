# -*- coding: utf-8 -*-
from requests import post

url = 'https://voting-vote-producer.r7.com/vote'

response = post(url)
print(response)
