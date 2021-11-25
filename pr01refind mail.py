
import re
fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name: ',fhand1)
    exit()
dict=dict()
for lines in fhand:
    lines=lines.strip()
    lines1=lines.split()
    if re.search('From:', lines1):
        print(lines1[6:])
