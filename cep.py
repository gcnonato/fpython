import requests

token = "a13c8b49453670f1a3ce7a15438c3af0"
headers = {'Authorization': 'Token token=%s' % token}


def search_by_cep(nro):
    url = f"http://www.cepaberto.com/api/v3/cep?cep={nro}"
    response = requests.get(url, headers=headers)
    return response.json()


def search_by_address():
    url = "http://www.cepaberto.com/api/v3/address?estado=SP&cidade=São Paulo&logradouro=Praça da Sé"
    response = requests.get(url, headers=headers)
    return response.json()


def search_cities():
    url = "http://www.cepaberto.com/api/v3/cities?estado=SP"
    response = requests.get(url, headers=headers)
    return response.json()


def search_by_cities():
    url = f"http://www.cepaberto.com/api/v3/address?estado=SP&cidade={'São+Paulo'}"
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == '__main__':
    # print(search_by_cities())
    # print(search_by_address())
    for key, value in search_by_cep(19034000).items():
        if 'cidade' in key or 'estado' in key:
            for k, v in value.items():
                print(f'{k} - {v}')
        else:
            print(f'{key} - {value}')


    # for city in search_cities():
    #     if 'aulo' in city['nome']:
    #         print(city['nome'])
