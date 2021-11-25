from sys import stdin, stdout
readline, writeline = stdin.readline, stdout.write


for _ in range(int(readline())):
    x, y = map(int, readline().split())
    d = y-x
    if d == 0:
        print(0)
    elif d > 0:
        if d % 2:
            print(1)
        elif not d % 2 and d % 4:
            print(2)
        else:
            print(3)
    else:
        if d % 2:
            print(2)
        else:
            print(1)
