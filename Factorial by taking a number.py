inp=int(input('Type in the number that you want to find thefatorial for: '))
factorial=1
if inp<0:
    print('Sorry factorial is not generated for Negative number:')
elif inp==0:
    print('Factorial for the number 0 is: 1')
else:
    for i in range(1, inp+1):
        factorial=factorial*i
    print('The Factotail for the Number',inp,'is :',factorial)
