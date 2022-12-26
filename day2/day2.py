"""
day2 控制流

author maverickpig

version 1


n = 5
while n > 0:
    n = n-1
    if n < 2:
        break
    print(n)

"""
for i in range(1,10000):
    n = i
    step = 0
    while n != 1:
        if n % 2 == 0:
            n = n //2
        else:
            n = n * 3 + 1
        step += 1
    else:
        print(i,'traped',step,'steps')