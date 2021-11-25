import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input('Enter URL: ') #Enter main URL
count = int(input('Enter count: ')) #The number of times to be repeated
posinput = int(input('Enter position: ')) - 1 #The position of link relative to first link

while count >= 0:
    html = urllib.request.urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print(URL)
    URL = tags[posinput].get("href", None)
    count = count - 1
