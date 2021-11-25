import re
hand = open('mbox.txt')

for line in hand :
    result= re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', line)
    if len(result)>0:
         print(result)
