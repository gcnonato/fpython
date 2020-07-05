import os

from tabula import convert_into, read_pdf

filename = 'CREDENCIADOS.pdf'
fileout = "output.csv"
homepath = os.path.expanduser(os.getenv('USERPROFILE'))
desktoppath = 'Desktop'
archive = os.path.join(homepath, desktoppath, filename)
output = os.path.join(homepath, desktoppath, fileout)
df = read_pdf(archive)
print(df)
