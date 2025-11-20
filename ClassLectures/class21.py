#Topic - lists
#Adding an item to a list - append()
#Matching items? - extende()
'''
listA = [1,2,3,4,5]
listB = [6,7,8,9,10]
listA.extend(listB) #extending together

listA.insert(3, "Apple") #Adding into a list
#listA.remove('a') #removing
popList = listA.pop(2) #remove the last character

print(popList)

#Task1 = printout just odd numbers into list??? 
numList = []
#for i in range (1, 50):
    #numList(i)


oddNums = [i for i in range(1,50,2)]
print(oddNums)

evenNums = [i for i in range (2,52,2)] #Printing 
print(evenNums)

import random as random
def randomOdd(x):
    if x%2!=0:
        return x #this will get us the value of odd num as 'none' - meaning it is even
    return x +1 #This will add the even to make it odd

oddNums = [random.randint(1, 25) for i in range (50) if ]
oddNums.count - this will count how many repeated numbers are into the list, this will also .....
oddNums.index - if we add together to count this will show the index of the count 
oddNums.sort() - if we have the count, index, and sort, this will print out in order from left to right - user .reverse if you want to print from right to left in left to right



def mExists (x):
    if 'm' in x:
        return x
names = ["Luis", "Jose", "Maria", "Alcala","Jessica", "Justin", "Monica", "Xochilt"] #Printing in ASCII value, higher value
print(names)
names.sort()
names.sort(key=len) #This will print the list with lowest amount of letters
#Lambda function?? - study
#names.sort(key=mExists) #we cannot sort a none, we have to have a value
sortedNames = sorted(names)
print(sortedNames)

evenNums = [i for i in range (2,201) if i%2 ==0]
#Task 2 - get average of the numbers above
print(evenNums)
print(sum(evenNums) / len(evenNums))  #use len instead of count()
#Task 3 = get the second largest number


#print(evenNums, sum(evenNums), max(evenNums), min(evenNums)) 

cities = ["Green Bay", "Appleton", "Sheboygan", "Madison", "Milwaukee", "La Crosse", "Oshkosh", "Shawana"]
#Task4 - find out how many 'o's in cities
def oCount (cities):
    count = 0
    for c in cities: #Accessing by value
        for l in c.lower(): #this will access the list and the characters 
            if l == 'o':
                count+=1
    return count  
print(oCount(cities))  

def letterCount (cities, x):
    count = 0
    for c in cities:
        for l in c.lower():
            if l ==x:
                count +=1
    print(f"The letter {x} was found {count} times")


vowels = ['a', 'e', 'i', 'o', 'u']
for v in vowels:
    letterCount (cities, v)
    '''
paragraph = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
def largeWord(paragraph):
    if ' ' in paragraph:
        paragraph = slice(paragraph)
    for c in paragraph: # accessing by value
