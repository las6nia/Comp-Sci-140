# class 11 - if conditions
import math as math
'''
num = int(input("Enter a number: "))
if num % 2 == 0 and num  % 5== 0:
    print("Number is even and divisible by 5")
else:
    print("odd number and not divisble by 5")

# While () looping until the condition is ssatifies, while matches with only one condition (until it satisfies something)



sum =0
num =1

#steps - initialize, num =1 sum=0. if the num is less than 10, update (num+=1), if you do not have a termination it will not reach to the stop sign

while(num<100):
    sum+=num
    num+=1
    print(sum)
print(sum)
#All iterations will print the sum if inside the while, while the sum outside the while
#FIX THIS
evenNum = int(input("Enter num: "))
while(evenNum<100):
    if evenNum% 2 == 0:
        evenNum +=1
    else:
        print("Enter a number less than 100")
else:
    print("Enter an even num")


total = 0
num =1

while(num<=100):
    if num % 2 == 0:
        total+=num
    num+=1
print(total)

#study (do while)
total =0
num = int(input("enter a number: "))
while num !=0: #sentinel value, the exit condition. Whule number is not 0
    total += num
    num = int(input("enter a number: "))

#try to find the largest number of multiple user inputs until the user reaches 0

total =0
num = int(input("enter a number: "))
largest = num
while num !=0: #sentinel value, the exit condition. Whule number is not 0
    num = int(input("enter a number: "))
    if num>largest: #Study!!
        largest = num #re-assignation of the num to the largest
print(largest)

#print number in a reverse order: if user puts 123, print 321
#mod function -- answer, if 234 , remainder of 4

#if 23/10 , remainder of 3
#Find a way to reverse it, multiplying but use 
#num1 = 123
#reverse = (num*2) - num 
'''
#reverse order of a number - 
num = int(input("Enter a number: "))
remainder = 0

while(num % 10):
    if (num != remainder):
        num = int(input("Enter a number: "))
        num = num % 10  #// 10


