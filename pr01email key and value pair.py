

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
        lines=lines[5]
        lines=lines[:2]
        dict[lines] = dict.get(lines, 0) + 1
        max(dict.values())
        key_max = max(dict.keys(), key=(lambda k: dict[k]))
lst = list()
for key, val in list(dict.items()):
    lst.append((key, val))
    x=sorted(dict.items())
for key, val in x[:]:
    print(key, val)
#print(dict)
#print('Maximum Value: ',dict[key_max])

#tmp=list()
#for k,v in dict.items():
#    x=sorted(dict.items())
#    print(x)

#largest = None
#print('Before:', largest)
#for itervar in [3, 41, 12, 9, 74, 15]:
#if largest is None or itervar > largest :
#largest = itervar
#print('Loop:', itervar, largest)
#print('Largest:', largest)
