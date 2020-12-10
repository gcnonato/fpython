import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Accept": "*/*",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Origin": "https://player.ec.cx",
    "Connection": "keep-alive",
    "Referer": "https://player.ec.cx/player3/canaishlb.php?canal=foxsports1&p=&fe=%27",
    "TE": "Trailers",
}

params = (
    ("expires", "1594869689"),
    ("token", "b26e19336275060ef16bf9b1379c8ee0"),
)

response = requests.get(
    "https://stream.ec.cx/a/hls1/foxsports1.m3u8", headers=headers, params=params
)
