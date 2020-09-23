#!/usr/bin/python3
import datetime
import PySimpleGUI as sg
from datetime import datetime, timedelta

from time import sleep
from decouple import config

from requests import Session, get


def get_date(data):
    try:
        if ":" in data:
            sep = ":"
        else:
            sep = "-"
        ano, mes, dia = [int(i) for i in data.split(sep)]
        return ano, mes, dia
    except:
        return None


def get_time(time):
    try:
        hours, minutes, seconds = [int(i) for i in time.split(":")]
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)
    except:
        return None


# def get_projects_in_rabbiit():
#     projects = []
#     for project in result['data']:
#         name ='-'.join((str(project['project_id']),project['project_name']))
#         projects.append(name)
#     print(set(projects))


def acessar_pagina():
    url = "https://app.rabbiit.com/api/v1/reports/detailed"
    token = login()
    headers = {"Authorization": f"token {token}"}
    response = get(url, headers=headers)
    return response.content


def logar(html, params):
    session = Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    # response = session.post(html, data=params, headers=headers)
    resul = session.get("https://app.rabbiit.com/a/e7635e19d341/#/projects/3")
    # resposta = re.findall("Backup", resul.text)
    return resul


def login():
    url = f'https://app.rabbiit.com/api/v1/auth?email={config("rabbiit_email")}&password={config("rabbiit_password")}'
    token = get(url).json()["token"]
    return token


def variables_to_access_site(token, month, year=2020, dayInitial='7', dayFinal='6'):
    # Quando for usar tem q entrar no site, e atualizar esse authorization pelo https://curl.trillworks.com/#python
    cookies = {
        "_ga": "GA1.2.581327304.1556565197",
        "_gid": "GA1.2.1016363647.1556565197",
        "a": "e7635e19d341",
        "a-e7635e19d341": "G2k2G6YDgcrfGnZ2ExtwIWDP6JQbLKDTjdUqAlKitMst-9ZVzmGPb3k48",
        "amplitude_idrabbiit.com": "eyJkZXZpY2VJZCI6ImE4OTQyMjQxLTU4ZjAtNDgwMS1hNzhhLWUzMzJmNjU5MzVlYlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU1NjU2NTIxNDk1NSwibGFzdEV2ZW50VGltZSI6MTU1NjU2NTQzODAxNywiZXZlbnRJZCI6NCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjR9",
        "intercom-session-686c4e3617bad5cdb7e55dfaaace8b455742041c": "SzQxV0xXci9LT2JQbzg1SVFabGlTZldpLzRZVk5iMUZhNThhak85azBDekJhcG13RnpVTEg3dkpCZmJGa054WS0tZkJKUmdKTEFHNXQ1Y01OeTN6VVJlQT09--fe775dde61c7fa780941c82201b7d1893d3bd0a9",
    }

    headers = {
        "authority": "app.rabbiit.com",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        "x-api-token": f"{token}",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.rabbiit.com/a/e7635e19d341/",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "a=e7635e19d341; a-e7635e19d341=SLGhk6Qh1MXpgiTyrEzEX0Sib0G8s5cIsqOPXxtQQJUz-J9p32AXNB6BY; intercom-session-686c4e3617bad5cdb7e55dfaaace8b455742041c=RVY2YXlvRG1oaXF0YkkvSU80dzhwL00zVG84Wlh1SXEzRWJQYTVySFdWT3VDTjBXcDJTaXJNamQ1Mmh3Um5nSS0tTU9aTUlhRzRjZDlaaWtNUjJhSzl4QT09--50e7c36c9d5ca69d99913c9de262fe1bd7006aa9",
    }
    if len(dayInitial) < 2:
        dayInitial = ''.join(("0",dayInitial))
    if len(dayFinal) < 2:
        dayFinal= ''.join(("0", dayFinal))
    month_present = ''.join(("0", month))
    month_previous = ''.join(("0", str((int(month)-1))))

    params = (
        ("date_execution_start", f"{year}-{month_previous}-{dayInitial}"),
        ("date_execution_end", f"{year}-{month_present}-{dayFinal}"),
        ("opt_sort_by", "date_execution"),
        ("opt_sort_direction", "asc"),
    )
    url = "https://app.rabbiit.com/api/v1/reports/detailed"
    return get(url, headers=headers, cookies=cookies, params=params)


def main(month, year, day_initial, day_end):
    token = login()
    response = variables_to_access_site(token, month, year, day_initial, day_end)
    result = response.json()["data"]
    return result


class Gui:
    def __init__(self):
        self.days = [str(days) for days in range(1, 32)]
        self.months = [
            "1:Janeiro",
            "2:Fevereiro",
            "3:Março",
            "4:Abril",
            "5:Maio",
            "6:Junho",
            "7:Julho",
            "8:Agosto",
            "9:Setembro",
            "10:Outubro",
            "11:Novembro",
            "12:Dezembro",
        ]
        self.years = [str(year) for year in range(2008, 2026)]

    def layout_inicial(self):
        sg.change_look_and_feel("Dark Blue 3")
        default_dayInicial = 7
        default_dayFinal = 8
        default_month = self.months[int(datetime.now().month - 1)]
        default_year = int(datetime.now().year)
        layout = [
            [
                sg.Combo(
                    self.days,
                    size=(10,12),
                    enable_events=False,
                    key="choicedayinicial",
                    default_value=default_dayInicial,
                )
            ],
            [
                sg.Combo(
                    self.days,
                    size=(10, 12),
                    enable_events=False,
                    key="choicedayfinal",
                    default_value=default_dayFinal,
                )
            ],
            [
                sg.Combo(
                    self.months,
                    size=(60, 12),
                    enable_events=False,
                    key="choicemonth",
                    default_value=default_month,
                )
            ],
            [
                sg.Combo(
                    self.years,
                    size=(60, 12),
                    enable_events=False,
                    key="choiceyear",
                    default_value=default_year,
                )
            ],
            [sg.Cancel(), sg.OK()],
            [sg.Multiline(font='Calibri', key='inicio', size=(100, 1), disabled=True, border_width='0')],
            [sg.Multiline(font='Calibri', key='return', size=(100, 10), disabled=True, border_width='0')],
            [sg.Multiline(font='Calibri', key='resultado_final', size=(100, 1), disabled=True, border_width='0')],
            [sg.Multiline(font='Calibri', key='fim', size=(100, 1), disabled=True, border_width='0')]
        ]
        window = sg.Window("Ganhos nos bicos", grab_anywhere=False).Layout(layout)
        while True:
            event, values = window.read()
            print(event)
            if "OK" in event:
                soma = 0.0
                project_name = "FreelaComAndré"
                totalHoras = timedelta(hours=0, minutes=0, seconds=0)
                month = values["choicemonth"]
                nro_month = str(month).split(':')[0]
                year = values["choiceyear"]
                day_initial = values["choicedayinicial"]
                day_end = values["choicedayfinal"]
                result = main(nro_month, year, day_initial, day_end)
                window['inicio'].update(f'Projeto Iniciado: {datetime.now()}')
                list_jobs = []
                for projeto in result:
                    get_project_name = projeto["project_name"]
                    ganhos_por_hora = projeto["rate_hour"]
                    if project_name in get_project_name:
                        year_job, month_job, day_job = get_date(projeto["date_execution"])
                        soma += float(projeto["rate_total"])
                        totalHoras += get_time(projeto["time_total"])
                        list_jobs.append(f'{day_job}-{month_job}-{year_job}')
                        list_jobs.append(f"{projeto['time_start']} - {projeto['time_end']} = {projeto['time_total']}")
                        list_jobs.append(f"Ganho nesse dia..: {projeto['rate_total']}")
                        list_jobs.append(f"Total de Horas..: {totalHoras}")
                        list_jobs.append(f"Total Ganho..: {round(soma, 3)}")
                        list_jobs.append(f'{"*"*90}')
                window['return'].update(list_jobs)
                window['resultado_final'].update(f'{round(totalHoras.total_seconds()/3600,2)} horas com {ganhos_por_hora} por hora ganhei R$ {round(soma, 3)} reais')
                window['fim'].update(f'Projeto Finalizado: {datetime.now()}')
            elif "Cancel" in event:
                sg.popup_auto_close("Exit...", auto_close_duration=0.5)
                break
        window.close()

gui = Gui()
gui.layout_inicial()
