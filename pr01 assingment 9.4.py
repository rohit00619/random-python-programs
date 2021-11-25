fhand1=input('Type in the file name you want to use: ')
d = dict()
fhand = open(fhand1)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]

    if email in d:
        d[email] += 1
    else:
        d[email] = 1

lst = d.values()
m = max(lst)

for address in d:
    if d[address] >= m:
        print(address, d[address])
