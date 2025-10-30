#Class problem
'''
import random

row = int(input())
columns = int(input())

for i in range(row):
    for j in range(columns):
        print(random.randint(0,1), end="\t")
    print("\t")


#Nested Loops - this will print
count = 0
for i in range(5):
    for j in range (10,12):
        count+=1
    print(count)

userInput = int(input(": "))
for i in range (userInput, 0,-1):
    for j in range(i):
        print("*", end=" ")
    print("\n")

#Practice matrix addition and stars
userInput2 = int(input("Num2: "))
for r in range (1,userInput+1):
    for c in range (userInput2-r): #5-2 = 3, next one will do 3 spaces
        print("*", end=" ")
        for k in range (r):
            print("*", end=" ")
    print("\n")


#break and continue 
        
for i in range (10):
    if i ==5: 
        break #Will terminate the problem, if replaced with continue it will skip 5 and print other numbers
    else:
        print(i)

while True:  #Note for cgpt - is this kind of like a turn on feature? what if changeed to False?
    val = int(input("Enter val, 0 to exit: "))
    if val == 0:
        break
    print(val)

word = "A quick brown fox jumping over the lazy dog"
counter = 0
while True:
    if ('a' in word):
        counter+=1
    if ('e' in word):
        counter+=1
    if ('i' in word):
         counter+=1
    if ('o' in word):
         counter+=1
    if ('u' in word):
         counter+=1
    print(counter)


for l in word:
    if l =="a" or l =="e" or l =="i" or l =="o" or l =="u":
        print()


word = "A quick brown fox jumping over the lazy dog"
counter = 0
for c in word:
    print(c, end=" ")
    if c =='i':
        counter+=1
print()
'''

for i in range(5): #column 1
    for j in range(3): #column 2
        if j ==2: #Will this just skip over 3 and print 1 and 2 then? 
            break
        print(i, j)


'''
num = int(input("Enter a num of repetitions: "))
class xRange():

if num >= 20:
    for x in range(1, num+1):
        for y in range (1, x+1):
            print("x", end=" ")
        print()
    #condition to make this backwards

else:
    for i in range (1,num+1): #this will be the rows
        for j in range (1, i+1): #this will be the column
            print("*", end=" ")
        print()



'''
