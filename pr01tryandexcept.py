fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name',fhand1)
    exit()
count=0
for line in fhand:
    if line.startswith('From:'):
        atpos=line.find('@')
        print(line[6:atpos])
