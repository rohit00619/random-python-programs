
fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name: ',fhand1)
    exit()
dict=dict()
print(dict)
for lines in fhand:
    if lines.startswith('From '):
        lines=lines.split()
        lines=lines[2]
        dict[lines] = dict.get(lines, 0) + 1
print(dict)
