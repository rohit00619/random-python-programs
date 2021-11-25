fname=input('Enter a File name please: ')
try:
    fhand=open(fname)
except:
    print('This file seems to be not there or the name is wrong please check')
    quit()
fhand=open(fname)
count= 0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There are ',count,'Subject lines in this file.')
