#last topic - nested loops and breaks
#What would this print?
'''
found = False
for i in range (3):
    for j in range (4):
        if i ==2 and j == 2:
            found = True
            break
    if found:
        print(found, i, j)
        break
    print(f"{i}, {j}")

for i in range(3):
    for j in range(3):
        if j ==2:
            continue
        print(f"{i},{j}") #Study this

#3 attempts in 
atmPin = "2345"

for i in range(3):
    atempt = i+1
    enteredPin = input("Enter your pin: ")
    if enteredPin == atmPin:
        print(f"Log in successful!, you took {atempt} tries!")
        break
    else:
        print(f"Try again, tries: {atempt} /3")
        if atempt == 3:
            print(f"Out of tries, Account locked after {atempt}, contact your bank")
            break
        continue
'''

#Functions, method, procedures - we use functions, avoid repeating yourself, user defined function to avoid repeating yourself
'''
                                        syntax - def func()
'''
'''
# do not use curly braces like in java
def adding():
    num1 = int(input("Enter num 1: "))
    num2= int(input("Enter num 2: "))
    result = num1+num2
    print(f"The sum of {num1} and {num2} = {result}") 
def func2():
    pass
#we call by name
adding()
#We you create your function first and then call your function
#We can also create a function to later call by using pass >>>func2 above<<
func2()

#What if i want to avoud 

def myNums():
    n1=int(input("Enter your first: "))
    n2=int(input("Enter your second: "))
myNums()
#print(n1+n2) # this is not going to declared out because it's inside the function, locally vissibly


num1 = int(input("Enter num 1: ")) #these numbers are included across the whole code
num2= int(input("Enter num 2: "))
def adding():
    result = num1+num2
    print(f"The sum of {num1} and {num2} = {result}") 






#2 When you define a function it will only be viewed inside a function but not outside
def addingEx(num3,num4): #Known as parameters a
    adding = num3 + num4
    print(f"The sum of {num3} + {num4} is {adding}")
#Do not call
def inputNum():
    num3 = int(input("Num3: "))
    num4 = int(input("Num3: "))
    addingEx(num3, num4) # this are called argument, this will have to have a placeholder to save it. 
    #error because it is not defined, I will place addingEx(n3,n4 before this now to have it work)
inputNum() #You can call this and will take the 'function' from the top 1
'''

pin = str(input("Enter pin: "))
correctPin = "1234"
car = 1
#Increase counter of car from the inside to the outside - Check and email before 10/30
def pinTries():
    for j in range(3):
        print(f"Vehicle {car} is approaching") 
        for i in range(3):
            atempt = i+1
            if pin == correctPin:
                print(f"Log in successful!, you took {atempt} tries!")
                break
            else:
                print(f"Incorrect PIN. Attempt {atempt}/3")
            car+=1

pinTries()
pinTries()

'''if car1 ==2:
    pinTries()
else:
    pinTries()'''


