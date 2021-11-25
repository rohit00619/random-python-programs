fhand1=input('Type a file name you want to use : ')
try:
    fhand=open(fhand1)
except:
    print('File Not Found Please enter a correct name: ',fhand1)
    exit()
count=0
intatpos=0
for lines in fhand:
    if lines.startswith('X-DSPAM-Confidence:'):
        count=count+1
        atpos=lines[20:]
        intatpos=float(atpos)+intatpos
print('Average spam confidence: ',intatpos/count)
