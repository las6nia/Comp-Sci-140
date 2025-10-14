num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 <= num2) and (num1 < num3):
    print(num1)
elif (num2 <= num1) and (num2 < num3):
    print(num2)
else:
    print(num3)

#class 11 - Loops

#ZYBOOKS ASSIGNMENT

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

counter = 0

if num1 % 2 > 0:
    counter+=1
if num2 %2 > 0:
    counter+=1
if num3 %2 > 0:
    counter+=1
if num4 %2 > 0:
    counter+=1
print(counter)
