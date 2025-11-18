numList= [1,2,3,4,5,6,7,8,9,10]

print(numList[0:5])
'''
print(numList[-2: :-2]) # In multipleCVhoice question

#things to learn from lists = add allNums(append)
numList.append('a')
#Adding at the end
numList(len(numList)) #returning as index? study this


print(len(numList))
numList[len(numList)-1] = 'b'
print(numList)
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12]
listAdd = list1+list2+list3
print(listAdd)
# C# is climbing up
#Inheritance = who should i inherit from? imagine a student has a class, is a student - what class should I be in? faculty, student, teaching assistance?

#What if a list has multiple elements?
import random
#Example 1:
randomNumber = [random.randint(1,1000) for i in range(100)] #this is list comprehencion (known in 1 list)
#print(randomNumber)
#Access by value
for v in randomNumber:
    print(v, end=" ")
#Example 2:
randomNumber2 = []
for i in range(1000):
    randomNumber2.append(random.randint(1,1000)) #Append, once it is called using append, the append function goes back and tries to fetch the result, im comparison, example 1 is more efficient than this

#Try ourselves - printing by index
randomNumberIndex = []
#for j in range (1000) :
 #   print(randomNumberIndex.append(random.randint(1,100)[j]))
    
#answer
#Access by index - 
for k in range (len(randomNumberIndex)):
    print(randomNumberIndex[k], end=" ")
    
#access by value AND index
#Fix
#for index,value in enumerate(randomNumber, randomNumberIndex):
 #   print(index, value)

#Automatically going through a list - functions for list
'''

#What if we want to add one list to another? using + 
#and also:
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# listMain = list1.extend(list2) #Why is it not printing? - previous topic - function but not doing anything - 
#Extend takes 1 list to list 2, list 2 will change - you can save a HARD COPY of the original list to not modify
print(list1)
print(list2)
#Deep copy - you have 
#Shallow copy = .copy() function
listTemp = list2
listTemp[1] = 15
#We will have the updated 
print(listTemp)


#Task = assume a website is 
website = "http://www.wikipedia.org/cheese/mozzarella"

#Write a function that takes this input and returns the original domain name as www.wikipedia.org
#print(len(website))
'''
#Practice
def lengthString():
    count = 0 
    for c in list1:
        count+=1
    return count


if 'http://' in website:
    print(website[6])    
for i in website:
    if 'http://' in website:
        website-= 'https://'
        print(website[0:1])
'''
#solution # Classwork 15 practice

print(website[0].split('/')[2].split('.')[2])
#List the name of the company

