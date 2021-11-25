name = input('Enter a File name: ')
handle = open(name)
counts= dict()
for line in handle:
    words= line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1

bigcount = None
Bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount= count
print(bigword, bigcount)
