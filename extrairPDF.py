
from tabula import read_pdf, convert_into
import os


filename = 'CREDENCIADOS.pdf'
fileout = "output.csv"
homepath = os.path.expanduser(os.getenv('USERPROFILE'))
desktoppath = 'Desktop'
archive = os.path.join(homepath, desktoppath, filename)
output = os.path.join(homepath, desktoppath, fileout)
#
# tables = wrapper.read_pdf("MyPDF.pdf",multiple_tables=True,pages='all')
#
# i=1
# for table in tables:
#     table.to_excel('output'+str(i)+'.xlsx',index=False)
#     print(i)
#     i=i+1

# read PDF as JSON
df = read_pdf(archive)
# convert PDF into CSV
# convert_into(archive, output, output_format="csv", pages='all')
print(df)

# convert_into(archive, "teste.json", output_format="json")
