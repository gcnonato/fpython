# -*- coding: utf-8 -*-
import os
from requests import get

homepath = os.path.expanduser(os.getenv("USERPROFILE"))
desktoppath = "Desktop"
local_save = os.path.join(homepath, desktoppath)
os.chdir(local_save)
for book in range(4, 6):
    url = f'https://lao-online.com/books/download/{book}.html'
    filename = f'books-{book}.pdf'
    with open(filename, "wb") as file:
        response = get(url, stream=True)
        file.write(response.content)
