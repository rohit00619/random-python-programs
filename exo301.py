min= None
max= None
num = 0
while True:
    sval= input('Enter a no: ')
    if sval =='done':
        break
    try:
        fval= int(sval)
    except:
        print('Invalid input')
        continue
    if min is None:
        min=sval
    elif min<sval:
        min=sval
    if max is None:
        max=sval
    elif max<sval:
        max=sval

print('Maximum is',max)
print('Minimum is',min)
