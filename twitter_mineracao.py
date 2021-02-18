import json
# from datetime import date

from TwitterSearch import TwitterSearch, TwitterSearchOrder
from decouple import config

iCONTADOR = 0
iCONT = 0
lista_full = []
lista_tweets = []
lat = -22.129517345580314
long = -51.391638801542605
km = 50

quantidade_para_interar = 200
subjects = ['STF']
# language = #'pt'

try:
    iCONECTA = TwitterSearch(
        f'{config("twitter_consumerkey")}', f'{config("twitter_consumersecret")}',
        f'{config("twitter_accesstoken")}', f'{config("twitter_accesstokensecret")}'
    )
    iATRIBUTO = TwitterSearchOrder()
    iATRIBUTO.set_keywords(subjects)
    # iATRIBUTO.set_language(language)
    # iATRIBUTO.set_geocode(lat, long, km, imperial_metric=False)
    # iATRIBUTO.set_since(date(2021, 1, 1))
    # iATRIBUTO.set_until(date.today())
    iATRIBUTO.set_result_type('mixed')  # mixed, popular recent

    for tweet in iCONECTA.search_tweets_iterable(iATRIBUTO):
        lista_full.append(tweet)
        lista_tweets.append(
            (
                ''.join(("@", tweet['user']['screen_name'])),
                tweet['user']['name'],
                tweet['text'],
                tweet['created_at'],
                tweet['source'],
                tweet['user']['description'],
                # tweet['user']['entities'], #['url'], #['urls']['display_url'],
                tweet['user']['entities']['description'],
                # ['url'], #['urls']['display_url'],
                tweet['user']['url'],
                tweet['user']['profile_image_url']
            )
        )
        iCONTADOR += 1
        if iCONTADOR > 4:
            break
    json_full = json.dumps(lista_full, indent=4, ensure_ascii=False)
    json_filtro = json.dumps(lista_tweets, indent=4, ensure_ascii=False)
    print(json_filtro)
except Exception as error:
    print(f'ERROR..: {error}')
