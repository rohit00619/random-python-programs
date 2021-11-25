import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
hey=input('give me a address: ')
fhand = urllib.request.urlopen(hey).read()
soup= BeautifulSoup(fhand,'html.parser')
tags=soup('a')
for tag in tags:
    print (tag.get('href',None))
