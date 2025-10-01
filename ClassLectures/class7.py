
#if statements 
age = 18
if age > 18:
    print("You can vote")
else:
    print("You cannot vote")

# when comparing, make sure you do types , string and int, and float



marks = 80
if marks >= 90:
    print("A")

        amount = int(input("Enter your amount: "))
        if amount >= 50:
            print(f"Your deposit is {amount}.")
        else:
            print("Enter a valid input: ")
            break


elif marks >=75:
        print("B")
elif marks >=60:
        print("C")
else:
        print("D")
#Iterations - study,ieration of 5          ******PRACTICE******

number = 0
if number > 0 :
    print('positive nuber')
elif number == 0 :
     print("value 0")               #this works but it's preferable to add positive, negative
else:
      print('Negative number')
    

age = 18
has_id = False

if age>=18:         #you can use if age>=18 and has_id == True will give you the most convenient
    if has_id == True:
         print("You are elegible to vote")
    else:
         print("You are not elegible to vote because you do not have an ID")
else:
     print(f"You cannot vote as you are less than {age}")




x = 12
y = 8
z = 15

if x>y and x<z:
    print('x is between y and z')
elif not x>y and x<z:
    print("X is NOT in between y and z")
    


                            #task - #which number is largest among these 3 inputs
value1 = int(input("Enter num 1: ")) 
value2 = int(input("Enter num 2: "))
value3 = int(input("Enter num 3: "))

if value1>value2 and value1 > value3:
    print("Value 1 is greater than value 2 and value 3")

if value2>value1 and value2 > value3:
    print("Value2 is greater than value 1 and value 3")
else:
    print("value3 is greater than value 1 and value 2")


year = int(input("Enter a year to see if it's leap or not: "))
isLeapYear = year % 4
isNotLeapYear = year % 100
if isLeapYear == 0 and isNotLeapYear >0 :
    print("your year is a leap year! ")
else:
    print("your year is not a leap year :(")

                        
                        #`task 2 - take the input of the age of a person and determine the age hroup of
                        #the person using the following condition
                        #age = 0-13 child
                        #age = 14-19 - teenager
                        #age 20 - 59 - adult
                        #age 60+ - senior 

age = int(input("enter your age: "))

if age<0:
    print("You are a todler!")
elif age >=0 and age <=13:
    print(f"you are a child as you are {age} years old!")
elif age >=14 and age <=19:
    print(f"you are a teenager as you are {age} years old!")
elif age >=20 and age <=59:
    print(f"you are an adult as you are {age} years old!")
else:
    print(f"you are a senior! yikes! you're {age}, gross!")

                        #canvas assignment - 
                        #FRIDAY QUIZ - Study!




