num=int(input('Type in your number: '))

def cube(num):
    sum1=0
    for i in range(1, num+1):
        sum1 += i*i*i
    return sum1
print(cube(num))
