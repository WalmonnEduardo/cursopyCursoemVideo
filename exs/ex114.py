import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.itaipuparquetec.org.br/')
except:
    print('Deu erro!')
else:
    print('Ok')
    print(site.read())