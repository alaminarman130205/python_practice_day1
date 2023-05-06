import math

print('for rounded and abs ')
x=2.9
print(round(x))
print(abs(-2.9))

print('rounded and abs end also math function start')
print('--------')

x=2.9
print(math.ceil(x))
print(math.floor(x))


print('end of ceil and floor start if else from here')

i = 20
if i == 10:
    print("i is 10")
elif i == 15:
    print("i is 15")
elif i == 20:
    print("i is 20")
else:
    print("i is not present")


print('end of if else starting comparison relational conditional operator ')

a = 9
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


print('end of these three and start logical operation----')
a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("at-least one number is not greater than 0")



print('end of logical operator and start numeric data type like complex number')
a=6+7j
print(a)
print(a.real)
print(a.imag)
print(type(a))

b=5+5j
print(a+b)


print('end of complex number start while loop')


count = 0
while count < 9:
   print('The count is:', count+1)
   count = count + 1

print("Good bye!")


i = 1
while i < 6:
  print(i)
  if i == 4:
    break
  i += 1


n = int(input("Enter the n Number:"))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i +1

print(sum)







