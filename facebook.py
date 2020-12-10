# coding:utf-8
import random
import time

import requests

token = "EAANtG5nmr70BAHYsogbTNpNvrdnumF4miWufZA50Ec2b24Dxip500PsXXvFuY2RrCZB33OD6UyZBZBN4kWDDlE0XDIZCchzOGL9llEFr" \
        "z2YYeGbGtEZAE90DoHH6RBoGyilwL2FwVbskvSJfeIh5v9ZClpGkue9XeNLPf8SZBNTkRevL9LOyMjBribqN9ybNQZBnAS087zq3dXRZBa" \
        "XJZAOQZCU5yqLcgBzHOEGMUH6uEKZCynwZDZD"


def req_facebook(req):
    r = requests.get("https://graph.facebook.com/v3.1/" + req, {"access_token": token})
    return r


req = "me?fields=last_name%2Cfirst_name"
results = req_facebook(req).json()
data = []
i = 0
while True:
    try:
        time.sleep(random.randint(2.5))
        data.extend(results["pagina"]["next"])
        # results = r.json()
    except Exception:
        print("done")
        break

# pickle.dump(data,open("steam_data.pkl","wb"))
# loaded_data=pickle.load(file=open("steam_data.pkl"))
