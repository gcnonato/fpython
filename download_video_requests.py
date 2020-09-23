from requests import get
import os
from tqdm import tqdm


def download_file(html, filename):
    homepath = os.path.expanduser(os.getenv('USERPROFILE'))
    desktoppath = 'Desktop'
    local_filename = os.path.join(homepath, desktoppath, filename)
    # NOTE the stream=True parameter below
    response = get(
        html,
        headers=headers,
        stream=True
    )
    print(f'Iniciando o downloads...\n')
    filelength = int(response.headers['Content-Length'])
    with response as r:
        r.raise_for_status()
        pbar = tqdm(total=int(filelength / 8192))
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                try:
                    if chunk:  # filter out keep-alive new chunks
                        pbar.update()
                        f.write(chunk)
                except Exception as err:
                    print(err)
    print(f'\nFinalizando o downloads...')
    return local_filename


# html = 'https://www93.o0-1.com/token=byaZxprjZBUaz5gQ3SzpNg/1600542849/201.42.0.0/58/4/d8/6127949f4de21a18b1a5feb26bbf9d84-360p.mp4'
html = 'https://www93.o0-1.com/token=iTlXm_IwcRjd0rHeXZ3Ucg/1600556091/201.42.0.0/58/4/d8/6127949f4de21a18b1a5feb26bbf9d84-360p.mp4'
header = html.split('/')[2]
print(header)
filename = 'Rua Augusta 12.mp4'

headers = {
    'authority': f'{header}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'video',
    'referer': 'https://playernetfilme.xyz/',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'range': 'bytes=0-',
}
download_file(html, filename)