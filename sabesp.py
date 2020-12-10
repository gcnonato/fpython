import requests
from pprint import pprint


session = requests.Session()

response = session.get(
    "https://www9.sabesp.com.br/agenciavirtual/pages/home/paginainicial.iface",
    timeout=30,
)


cks = session.cookies

JSESSIONID = session.cookies.get_dict()["JSESSIONID"]
print(cks)
print(type(JSESSIONID))
# cookies = session.cookies.get_dict()

cookies = {
    "JSESSIONID": "0001MyZnLTQQ0lSMNX3_qXDFoc0:18du7alf0",
    "ice.sessions": "fYZBPVcNj0F3VMItQKPyRQ#1",
}

headers = {
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept": "*/*",
    "Origin": "https://www9.sabesp.com.br",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www9.sabesp.com.br/agenciavirtual/pages/home/paginainicial.iface",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

data = {
    "$ice.submit.partial": "false",
    "ice.event.target": "",
    "ice.event.captured": "frmhome:j_id308",
    "ice.event.type": "onclick",
    "ice.event.alt": "false",
    "ice.event.ctrl": "false",
    "ice.event.shift": "false",
    "ice.event.meta": "false",
    "ice.event.x": "620",
    "ice.event.y": "259",
    "ice.event.left": "false",
    "ice.event.right": "false",
    "dsMenu": "",
    "outcomeSubMenu": "",
    "frmhome:_idcl": "frmhome:j_id308",
    "cdNoticia": "",
    "outcomeMenu": "",
    "cdMenu": "",
    "frmhome:rgi1": "0501350403",
    "frmhome:j_id298": "562",
    "frmhome:listaFunc": "1",
    "": "paginainicial",
    "frmhome:menuID": "0",
    "javax.faces.RenderKitId": "ICEfacesRenderKit",
    "javax.faces.ViewState": "11",
    "icefacesCssUpdates": "",
    "frmhome": "frmhome",
    "ice.session": "pZ6lfgSjqKFX-nxbn3unzg",
    "ice.view": "11",
    "ice.focus": "",
    "rand": "0.41048845916618926\\n\\n",
}

response = requests.post(
    "https://www9.sabesp.com.br/agenciavirtual/block/send-receive-updates",
    headers=headers,
    cookies=cookies,
    data=data,
)
pprint(response.content)
