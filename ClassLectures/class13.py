'''
sentence = "A quick brown fox"

for c in range(len(sentence)): #len of sentence
    if sentence[c] == " ":
        print(sentence[c], end="")
    elif c == 0:
        print(ord(sentence[c]+11))
    else:
        print(sentence[c])
print(sentence)


#answer


# the program will calculate the sequence up to a particular  index
#print up to 4th index, write down 1,1,2,3,
# if up to 6th
#fibonnaci sequence???? 1
userInput = int(input("Enter your # "))
myList = [1,2,3,4,5,6,7,8]
if userInput <= 8:
    previousNum = 
    lookedNumber = (myList[userInput]-[])

print(lookedNumber)
#classwork10


#for loops are more easy
for i in range(1,50, 3):
    print(i, end=" ")

#now in while

j = 1
while j <= 50: #condition check
    j+=3
    print(j, end=" ")

#nested loops

for outter_variable in outerSequence:
    for innerVariable in innerSequence:

        #body of action
#while inside a while
letter1 = "a"
letter2 = "?"
while letter1<="f":
    letter2 = "a"
    while letter2<="f":
        print(f"{letter1}{letter2}.com")
        letter2=chr(ord(letter2)+1) #update for second while loop
    letter1 = chr(ord(letter1+1)) #Update to first while #convert to unicode and character


#for inside a while
num = 0
while(num>=0):
    num= int(input("Enter a num(negative to quit): "))
    if num>=0:
        print("Graphical representation")
        for i in range (num):
            print("*", end=" ")
        print('\n')
print("goodbye")



#first number is row(add new line)
for i in range (3):  #for rows
    for j in range(5): #for columns
        #matrix idea, 
        print(f"{i},{j} \t",end=" ")
    print("\n")
'''

#2 dimentional table based on user table

userInput1 = int(input("Enter your rows: "))
userInput2 = int(input("Enter your columns: "))

for i in range (userInput1):  #for rows
    
    for j in range(userInput2): #for columns
            print(f"*\t",end=" ")
            #assign the userInt to equal the start
            #complete before the end of the day
    print("\n") 
