# -*- coding: utf-8 -*-
from requests import get
from time import sleep
import json
import os
from decouple import config


class TelegramBot:
    def __init__(self):
        self.url_base = f'https://api.telegram.org/bot{config("TOKEN_TELEGRAM")}/'

    def Start(self):
        update_id = None
        while True:
            update = self.get_news_message(update_id)
            datas = update["result"]
            if datas:
                for data in datas:
                    update_id = data["update_id"]
                    message = data["message"]["text"]
                    chat_id = data["message"]["from"]["id"]
                    is_first_message = int(data["message"]["message_id"]) == 1
                    response = self.create_response(message, is_first_message)
                    self.responder(response, chat_id)
            resultado = get(self.url_base)
            sleep(10)

    # Get messages
    def get_news_message(self, update_id):
        link_request = f"{self.url_base}getUpdates?timeout=100"
        if update_id:
            link_request = f"{link_request}&offset={update_id + 1}"
        result = get(link_request)
        return json.loads(result.content)

    # Create a response
    def create_response(self, message, is_first_message):
        if is_first_message == True:
            return f"""Olá bem vindo ao nosso BOT DE SCRIPTS"""
        elif message == "/clima":
            clima = Climatempo()
            dados = clima.main()
            hoje = dados[0]
            amanha = dados[1]
            dt_hoje = hoje['date_br']
            dt_amanha = amanha['date_br']
            return f"""{dt_hoje}
Probabilidade: {hoje['rain']['probability']}%-{hoje['rain']['precipitation']}mm
{hoje['text_icon']['text']['phrase']['reduced']}
Sensação Térmica.:{hoje['thermal_sensation']['min']}-{hoje['thermal_sensation']['max']}
Temperaturas:{hoje['temperature']['min']}-{hoje['temperature']['max']}
{'*' * 30}
{dt_amanha}
Probabilidade: {amanha['rain']['probability']}%-{amanha['rain']['precipitation']}mm
{amanha['text_icon']['text']['phrase']['reduced']}
Sensação Térmica.:{amanha['thermal_sensation']['min']}-{amanha['thermal_sensation']['max']}
Temperaturas:{amanha['temperature']['min']}-{amanha['temperature']['max']}
{'*' * 30}
"""
        elif message == 'help':
            return f"""Escolha entre: {os.linesep}
clima = Climatempo{os.linesep}
royale = Clash Royale{os.linesep}"""
        else:
            return f"""Escolha entre: {os.linesep}
/clima = Climatempo{os.linesep}
/royale = Clash Royale{os.linesep}"""

    # Responder
    def responder(self, response, chat_id):
        link_requisicao = (
            f"{self.url_base}sendMessage?chat_id={chat_id}&text=\n{response}"
        )
        get(link_requisicao)


class Climatempo:
    def __init__(self):
        self.sitePrincipal = f'http://apiadvisor.climatempo.com.br'
        self.token = 'f0c3f4079a3a59a24962861c24c8cd88'
        self.city = 'Presidente Prudente'

    def descobrir_id_da_cidade_para_usar_na_url(self, name_city, token):
        '''Retorna o código da cidade'''
        site = f'{self.sitePrincipal}/api/v1/locale/'
        site += f'city?name={name_city}&state=SP&token={token}'
        return (get(site)).json()

    def trazer_as_infos_do_tempo(self, _id, token):
        '''Passando o ID da cidade e o TOKEN temos as infos do tempo'''
        site = f'{self.sitePrincipal}/api/v1/forecast/locale/'
        site += f'{_id}/days/15?token={token}'
        retorno = get(site)
        return retorno.json()


    def main(self):
        info = self.descobrir_id_da_cidade_para_usar_na_url(self.city, self.token)
        result = self.trazer_as_infos_do_tempo(info[0]['id'], self.token)
        return result['data']

bot = TelegramBot()
bot.Start()
