
import re
fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name: ',fhand1)
    exit()
count=0
line=list()
for lines in fhand:
    lines=lines.rstrip()
    x=re.findall('^New\s\S+:\s([0-9][0-9][0-9][0-9][0-9])+',lines)
    if len(x)>0:
        print(x)
    line.append()
        count=count+1
print(count)
