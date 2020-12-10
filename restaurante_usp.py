from requests import post

headers = {
    "authority": "uspdigital.usp.br",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "content-type": "text/plain",
    "accept": "*/*",
    "origin": "https://uspdigital.usp.br",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://uspdigital.usp.br/rucard/Jsp/cardapioSAS.jsp?codrtn=19",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "JSESSIONID=759A44985A5CB33753119E1A0C054E3D; DWRSESSIONID=$$cHGUA$xN69qjKpKBPg$r4l5bn; "
              "NSC_mcwt_svdbse=ffffffff096cd06c45525d5f4f58455e445a4a4229a0; "
              "NSC_mcwt_dpnvnxfcefw=ffffffff096cd0e845525d5f4f58455e445a4a423660; "
              "NSC_mcwt_xtvtvbsjp=ffffffff096cd0be45525d5f4f58455e445a4a4229a0",
}

data = {
    "batchId": 1,
    "callCount": 1,
    "c0-param0": "string:19",
    "instanceId": 0,
    "c0-scriptName": "CardapioControleDWR",
    "c0-methodName": "obterCardapioRestUSP",
    "callCount": 1,
    "scriptSessionId": "$$cHGUA$xN69qjKpKBPg$r4l5bn/pM7m5bn-HStgR4BS4",
    "page": 2,
    "windowName": "",
    "c0-id": 0,
}

url = "https://uspdigital.usp.br/rucard/dwr/call/plaincall/CardapioControleDWR.obterCardapioRestUSP.dwr"

html = post(url, headers=headers, data=data)

texto = html.text
for tx in texto.split("cdpdia"):
    print(tx)
