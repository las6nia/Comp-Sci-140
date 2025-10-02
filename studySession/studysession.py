'''
#task 1 - Write a program that asks for someone’s age. If they are 18 or older, print "You can vote". Otherwise, print "You cannot vote".
age = int(input("enter your age: "))
if age >= 18:
    print("you can vote!")
else:
    print("You cannot vote")


#task 2 - comparison & Types What happens if you compare "18" (string) with 18 (integer) in Python? Write a program that checks if a number stored in x is equal to "10" (string).
x = "18"
x2 = 18
if x == x2:
    print(f"your value is {x+x2}")
else:
    print("The data type does not match")


#3. Grading Ask for a student’s marks (0–100). Print "A" if marks are 90 or above. "B" if 75–89. "C" if 60–74. "D" otherwise.
grade = int(input("Enter your grade as num: "))
if grade >= 90:
    if grade <=93:
        print("your grade is an AB!")
    elif grade >=101:   
        print("you're just flexing at this point")
    else:
        print("your grade is an A!!!")
        
elif grade >=80:
    print(f"Talk to me when you're a doctor, you got a B. your score was {grade}")
elif grade >=70:
    print(f"Your grade is C! practice more... your score was {grade}")
elif grade >=60:
    print(f"You barely made it! your score was {grade}")
else:
    print(f"You're a complete disapoinment! your score was {grade} and your grade is an F")


#4. Nested If Ask for a person’s age and if they have an ID card. Only print "You can vote" if they are 18+ and they have an ID. Otherwise explain why they cannot vote.
import time
age = int(input("Enter your age: "))
canVote = bool(input("Do you have an ID with you? enter Y / N: "))
# need help turning string to boolean!!!
y = True
n = False



if age >= 18 and canVote == (y):
    print("you are able to vote!")
elif age>=18 or canVote  == (n):
    print("You are 18 but do not have a photo ID")
    time.sleep(.4)
    print("try again later")
elif age <18:
    if canVote == 'n':
        print("you do not have an ID")
    else: 
        print("you are under 18")


#5. Largest of 3 Numbers Take three numbers as input. Print which one is the largest.
number1 = int(input("Enter your first Number: "))
number2 = int(input("Enter your second Number: "))
number3 = int(input("Enter your third Number: "))

if number1 > number2 and number1 > number3:
    print("number 1 is greater than number 2 and number 3")
elif number2 > number1 and number2 > number3:
    print("number 2 is greater than number 1 and number 3")
else:
    print("number 3 is greater than number 1 and number 2")

# 6. Leap Year Ask for a year. Check if it is a leap year using the correct rules: Divisible by 400 → leap year Divisible by 4 but not by 100 → leap year Otherwise → not leap year

year = int(input("enter your years to see if it's leap: "))

isLeap = year % 4
isNotLeap = year % 100

if isLeap == 0 and isNotLeap >= 0:
    print("your year is leap!")
else:
    print("your year is NOT a leap year! :(")


# 7. Age Groups Take a person’s age as input. Child: 0–13 Teenager: 14–19 Adult: 20–59 Senior: 60+

age = int(input("Enter your age: "))

if age <=13:
    print(f"you are a child as you are {age} years old!") 
elif age <= 19:
     print(f"you are a teenager as you are {age} years old!")
elif age <= 59:
      print(f"you are an adult as you are {age} years old!")
else:
      print(f"you are a senior as you are {age} years old!") 

#8. Logical Operators Write a program with three numbers x, y, z. Print "x is between y and z" if x is greater than y and less than z. Otherwise print "x is NOT between y and z".

x = int(input("enter first num: "))
y = int(input("enter second num: "))
z = int(input("enter third num: "))
if x >y and x < z:
    print(f"X{x} is between y{y} and z{z}")
elif y>x and y<z:
    print(f"y{y} is between x{x} and z{z}")
else:
     print(f"z{z} is between x{x} and y{y}")


#9. Positive, Negative, or Zero
user_input = int(input("Enter a number: "))
if user_input > 0:
    print("positive number")
elif  user_input < 0:
    print("Negative number")
else:
    print("Number is zero")
'''
#10. Challenge Ask the user for a number. If the number is divisible by both 3 and 5, print "FizzBuzz". If only divisible by 3, print "Fizz". If only divisible by 5, print "Buzz". Otherwise, print the number itself.
user = int(input("enter a number: "))

if user % 3 and not user % 5 != 0:
    print("Fizz")
elif user % 3 == 0  and user % 5 == 0:
     print("FizzBuzz")
else:
    print("Buzz")
  #need help

























inputNumber = int(input("Enter your number: "))

if inputNumber %3 == 0 and not inputNumber % 5 == 0 :
    print("Fizz")
elif inputNumber % 5 == 0 and not inputNumber %3 == 0:
    print("Buzz")
else:
    print("FizzBuzz")

