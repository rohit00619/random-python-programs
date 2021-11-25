# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
x=0
y=0
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
#   print ('TAG:',tag)
 #  print ('URL:',tag.get('', None))
  # print ('Contents:',tag.contents[0])
   #print ('Attrs:',tag.attrs)
   x=x+int(tag.contents[0])
   y=y+1
print('Count',y)
print('Sum',x)
