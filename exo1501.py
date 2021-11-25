import urllib.request, urllib.error, urllib.parse
from bs4 import *
import re
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input('Tpye a URL: ')
html=urllib.request.urlopen(url, context=ctx).read()
Soup= BeautifulSoup(html,'html.parser')

tags = Soup('a')
for tag in tags:
        print(tag.get('href', None))
            for tag18 in tags:
            print(tag18.get('[7]', None)
