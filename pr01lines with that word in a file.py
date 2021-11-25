
import re
fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name: ',fhand1)
    exit()
regularinput=input('Type something that you wanted to search: ')
count=0
for lines in fhand:
    lines=lines.rstrip()
    if re.findall(regularinput, lines):
        count=count+1

print('There are ',count, 'lines in the file with the word starting with', regularinput)
