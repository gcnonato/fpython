import requests

instas = ['carlabigatto','bell_nunes','katireis']


def instagram(perfil):
    response = requests.get(f'https://www.instagram.com/{perfil}/?__a=1').json()
    user_info = response['graphql']['user']
    print(user_info['username'])
    print(user_info['id'])
    print(user_info['profile_pic_url'])


for cada in instas:
    instagram(cada)
