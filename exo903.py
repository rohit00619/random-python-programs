fname= input('Enter a File Name: ')
if len(fname)<1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand:
    line= line.rstrip()
    #print(line)
    words = line.split()
    #print(words)
    for w in words:
        di[w] = di.get(w,0)+1
        #print(w, 'new', di[w])
#print(di)

largest = -1
for k,v in di.items():
    print(k,v)
    if v> largest:
        largest= v
        theword = k
print(theword, largest)
