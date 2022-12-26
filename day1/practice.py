"""
基本数据类型-上机练习

author： maverickpig

version：1

s = 'abcdefg12345'
print(s[3:-3])
print(len(s))
print(s[0:len(s)-2:2])


t = 'mike and tom'
a = t.split(' ')
print(a)
for i in a:
    print(i.upper(),end=' ')
t.replace('mike','jerry')
print('\n')
print(t)

num = [1,2,3,9,4,5,6,6]
num.reverse()
num.sort()
print(num)
num.append(1)
num.pop()
print(num)
print(num.index(9))
print(num.count(6))
num2 = [2,13,4,5,6]
print(num + num2)
print(num * 2)
print(num[1:4:2])
num.append('1')
print(num)
print(num[::-1])
print(6 in num)
print(sum(num))

student = {'name':"tom","age":20,"gender":"male","course":['math','computer']}
a = 'name' in student
print(a)
print(20 in student)
print(20 in student.values())

a = set()
a.add(2)
a.update({2, 3, 4, 5, 2})
a.pop()
print(len(a))
print(a)

x = int(input('as = '))
print(x)
num  = [1,2,3,4,5,6]
for i in num:
    print(i,sep=',')

"""

mylist = [1,2,3,4,5]
print(mylist[1:4])
print(mylist[-3:-6:-1])
print(mylist[0:5:2])

