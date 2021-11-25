def sum(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return xy

print('Select Operation:')
print('1 for Addition')
print('2 for Substraction')
print('3 for Multiplication')
print('4 for Division')

choice=input('Enter your Operation: ')

num1=float(input('Type your First Number'))
num2=float(input('Type your Second Number'))

if choice=='1':
    print(num1,'+',num2,'is', sum(num1,num2))
elif choice=='2':
    print(num1,'-',num2,'is', substraction(num1,num2))
elif choice=='3':
    print(num1,'*',num2,'is', multiplication(num1,num2))
elif choice=='4':
    print(num1,'/',num2,'is', division(num1,num2))
else:
    print('Invalid Input')
