import datetime
import re
from pprint import pprint
from time import sleep

from requests import Session, get, post


def variables_to_access_site(token):
    cookies = {
        '_ga': 'GA1.2.581327304.1556565197',
        '_gid': 'GA1.2.1016363647.1556565197',
        'a': 'e7635e19d341',
        'a-e7635e19d341': 'G2k2G6YDgcrfGnZ2ExtwIWDP6JQbLKDTjdUqAlKitMst-9ZVzmGPb3k48',
        'amplitude_idrabbiit.com': 'eyJkZXZpY2VJZCI6ImE4OTQyMjQxLTU4ZjAtNDgwMS1hNzhhLWUzMzJmNjU5MzVlYlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NjU2NTIxNDk1NSwibGFzdEV2ZW50VGltZSI6MTU1NjU2NTQzODAxNywiZXZlbnRJZCI6NCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjR9',
        'intercom-session-686c4e3617bad5cdb7e55dfaaace8b455742041c': 'SzQxV0xXci9LT2JQbzg1SVFabGlTZldpLzRZVk5iMUZhNThhak85azBDekJhcG13RnpVTEg3dkpCZmJGa054WS0tZkJKUmdKTEFHNXQ1Y01OeTN6VVJlQT09--fe775dde61c7fa780941c82201b7d1893d3bd0a9',
    }

    # Quando for usar tem q entrar no site, e atualizar esse authorization pelo https://curl.trillworks.com/#python
    # headers = {
    #     'Authorization': f'Bearer {token}',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,vi;q=0.6',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    #     'Accept': 'application/json, text/plain, */*',
    #     'Referer': 'https://app.rabbiit.com/a/e7635e19d341/',
    #     'Connection': 'keep-alive',
    # }

    headers = {'Authorization': f'Bearer {token}'}

    # params = {
    #     'date_execution_end': '2019-12-31',
    #     'date_execution_start': '2019-01-01',
    #     'opt_sort_by': 'date_execution',
    #     'opt_sort_direction': 'asc',
    # }
    url = 'https://app.rabbiit.com/api/v1/reports/detailed'
    resultado = get(url, headers=headers, cookies=cookies)
    return resultado

def get_date(data):
    try:
        if ':' in data:
            sep = ':'
        else:
            sep = '-'
        ano, mes, dia = [int(i) for i in data.split(sep)]
        return ano, mes, dia
        # return date(ano, mes, dia)
    except:
        return None

def get_time(time):
    try:
        hours, minutes, seconds = [int(i) for i in time.split(':')]
        return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        # return hours, minutes, seconds
    except:
        return None

def get_projects_in_rabbiit():
    projects = []
    for project in result['data']:
        name ='-'.join((str(project['project_id']),project['project_name']))
        projects.append(name)
    print(set(projects))

def logar(html, params):
    # r = post(html, data=params)
    session = Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    response = session.post(html, data=params, headers=headers)
    resul = session.get('https://app.rabbiit.com/a/e7635e19d341/#/projects/3')
    resposta = re.findall('Backup', resul.text)
    return resul


def login():
    params = {
        'email': '',
        'password': ''
    }
    html = 'https://app.rabbiit.com/api/v1/auth'
    token = get(html, params).json()['token']
    return token

def acessar_pagina():
    # url = 'https://app.rabbiit.com/a/e7635e19d341/#/projects/3'
    url = 'https://app.rabbiit.com/api/v1/reports/detailed'
    token = login()
    headers = {'Authorization': f'token {token}'}
    response = get(url, headers=headers)
    return response.content

def main():
    soma = 0.0
    today = datetime.date.today()
    # project_id = 7
    project_name = 'FreelaComAndré'
    token = login()
    response = variables_to_access_site(token)
    result = response.json()['data']
    totalHoras = datetime.timedelta(hours=0, minutes=0, seconds=0)
    # day_today, month_today, year_today = get_date(today)
    if today.month == 1:
        month_previous = 12
    else:
        month_previous = today.month - 1
    # print(month_previous)
    # return
    day_initial = '08'
    day_final = '07'
    # date_initial = day_initial/month_previous/year
    # date_final = day_final/today.month/year
    for projeto in result:
        get_project_name = projeto['project_name']
        print(get_project_name)
        if 'FreelaComAndré' in get_project_name:
            year_job, month_job, day_job = get_date(projeto['date_execution'])
            print(year_job, month_job, day_job, month_previous)
            if month_job == month_previous:
                soma += float(projeto['rate_total'])
                totalHoras += get_time(projeto['time_total'])
                print(f"{day_job}, {month_job}, \
                {projeto['time_start']}, \
                {projeto['time_end']}, \
                {projeto['time_total']}, \
                {projeto['rate_total']} {round(soma, 3)} {totalHoras}")
                sleep(1)
    print(f' \
          No total de {totalHoras} horas tive ganho de: R$ {round(soma, 3)} reais'
    )


if __name__ == '__main__':
    mes = [1,2,3,4,5,6,7,8,9,10,11,12]
    try:
        # token = login()
        # response = variables_to_access_site(token)
        # acessar_pagina()
        # result = response.json()
        main()
    except Exception as err:
        print(f'Error..: {err}')
