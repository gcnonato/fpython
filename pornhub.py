from pornhub_api import PornhubApi
import random
import string
from pprint import pprint

api = PornhubApi()
list_categories = []

# tags = random.sample(api.video.tags("l").tags, 5)
# category = random.choice(api.video.categories().categories)
# result = api.search.search(ordering="mostviewed", tags=tags, category=category)
cont = 0
categories = api.video.categories()#.categories
# print(category)
# for letra in list(string.ascii_lowercase):
#     for tags in api.video.tags(letra).tags:
#         if 'sandra nova' in tags:
#             print(api.search.search(ordering="mostviewed", tags=tags, category=category))
#             cont += 1
#             # print(tags)
#             print(cont)
quantity = 0
for category in categories:
    quantity += 1
    list_categories = [e.category for e in category[1]]

for category in list_categories:
    if 'amat' in category:
        print(category)
