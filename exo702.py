fname = input('Please Enter the File name: ')
fhand = open(fname)

for lx in fhand:
    ly=lx.rstrip()
    print(ly.upper())
