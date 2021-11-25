

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
        atpos=lines.find('@')
        lineat=lines[atpos+1:]
        dict[lineat] = dict.get(lineat, 0) + 1


print(dict)


#largest = None
#print('Before:', largest)
#for itervar in [3, 41, 12, 9, 74, 15]:
#if largest is None or itervar > largest :
#largest = itervar
#print('Loop:', itervar, largest)
#print('Largest:', largest)
