import urllib.request, urllib.parse, urllib.error
import ssl
import json


url = input("Enter location: ")
print ("Retrieving ", url)
xml = urllib.request.urlopen(url).read()
print ("Retrieved" ,len(xml),"characters")
json1 =  json.loads(xml)

sum=0
total=0


for counts in json1['comments']:
    sum += int(counts['count'])
    total += 1

print('Count:',total)
print( "Sum:", str(sum))
