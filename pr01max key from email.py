
fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name: ',fhand1)
    exit()
dict=dict()
for lines in fhand:
    if lines.startswith('From '):
        lines=lines.split()
        lines=lines[1]
        dict[lines] = dict.get(lines, 0) + 1
        max(dict.values())
        max1=max(dict.values())
        key_max = max(dict.keys(), key=(lambda k: dict[k]))

print(max1)
print(dict[key_max])
