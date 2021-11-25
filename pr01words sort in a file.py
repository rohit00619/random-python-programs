fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    if fhand1=='boo':
        print('Boo Hoo Hoo')
    else:
        print('File Not Found Please enter a correct name: ',fhand1)
    exit()
lst=[]
count=0
for lines in fhand:
    lines=(lines.rstrip()).lstrip()
    lines=lines.split()
    for word in lines:
        if word not in lst:
            lst.append(word)
    lst.sort()
print(lst)
