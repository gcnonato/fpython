import os
from io import BytesIO
from shutil import copyfileobj

from bs4 import BeautifulSoup as bs
from requests import get

html = get("http://noespacovip.com.br/imagem_fck/image/")
soup = bs(html.content, "html.parser")


def download_file(name, url, pasta):
    os.makedirs(pasta, exist_ok=True)
    xpto = get(url, stream=True)
    # with open(name, 'wb') as f:
    #     copyfileobj(xpto.raw, f)
    with open(f"{pasta}/{name}", "wb") as f:
        #     copyfileobj(xpto.raw, f)
        copyfileobj(BytesIO(xpto.content), f)
    # imageFile = open(os.path.join(diretorio, xpto), 'wb')
    # for chunk in res.iter_content(100000):
    #     imageFile.write(chunk)
    # imageFile.close()


# images = [i.a['href'] for i in soup.findAll('div', class_="thumbnail-image")]
images = [i.getText() for i in soup.find_all("a")]

url = "http://noespacovip.com.br/imagem_fck/image/"
for image in images[2:10]:
    # _image = image.split('/')
    name = image.split("/")[-1].strip()
    # pasta = '_'.join([_image[4], _image[5], _image[6]])
    homepath = os.path.expanduser(os.getenv("USERPROFILE"))
    desktoppath = "Desktop"
    base_dir = os.path.join(homepath, desktoppath, "images")
    print(name)
    # print(pasta)
    # download_file('{}.jpg'.format(image[0]), image, pasta)
    download_file(name, url, base_dir)
print(len(images))
