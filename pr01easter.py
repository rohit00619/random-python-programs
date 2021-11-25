fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    if fhand1=='boo':
        print('Boo Hoo Hoo')
    else:
        print('File Not Found Please enter a correct name: ',fhand1)
    exit()
count=0
for lines in fhand:
    if lines.startswith('Subject'):
        count=count+1
print('There were ', count,'Subject Lines in this file')
