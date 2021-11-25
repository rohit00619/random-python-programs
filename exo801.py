fh = open('mbox.txt')
for line in fh :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email=words[1]
    pieces= email.split('@')
    print(pieces[1])
