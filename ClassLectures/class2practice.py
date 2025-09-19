'''
# Num1 - Ask the user for two numbers, convert them to integers, and print their sum.
interger1 = int(input("Enter a number: "))
interger2 = int(input("Enter a second number: "))
sum = interger1 + interger2
print("your sum is:",sum)


# num2 - task 2 - Take two integers from the user and print a sentence showing their sum.
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))

print("your first numer is",num1, "and your second number is",num2,"\n","Which equals to",num1+num2)

#num3 - task 3 - Fix this code so it works correctly:
age = int(input("Enter your age\n"))
print("next year you will be:",age + 1)

#num4 - task 4 - fix the code: 

a = int(input("enter first value: \n"))
b = int(input("Enter second value: \n"))
c = int(input("Enter a third Number: \n"))
print(c+a)

#num5 - task 5 - Write a program that divides two numbers entered by the user. Handle the case when the second number is zero.

#GET HELP
# !!!!!!SOLVED!!!!!!
#explination - an 'if' statement was needed, if the second number equals (==) 0, the message will print
#"Enter a higher number", however, since it is not a loop, it will not give us the chance to try again,
#Since it can only be run once, we have to run again but it will not display correct logic,
#calculator: 10/0 = undefined, 0/10 = 0
first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))

if second_number == 0:
    print("Enter a higher number than 0")
else:
    divide = (first_number/second_number)
    print(divide)




# Task 6 - Ask the user for the length and width of a rectangle. Print both values and the area of the rectangle.
length = float(input("enter a value: ")) #h
width = float(input("Enter a width: ")) #b
area = (length*width)

print("The length is",length,"and the width is",width,)
print("the area is",area)

# Task 7 - Using a = 3 and b = 2, print sentences that show their sum, subtraction, multiplication, and division.

a = 3
b = 2
sum = a+b
subtract = a-b
multiplication = a*b
division = a/b
print("The sum is",sum)
print("The subtraction is",subtract)
print("The multiplication is",multiplication)
print("The division is",division)


# Task 8 -Predict and then run these expressions:

result1 = ('4' * '10')
print("this will print an error due that you cannot display a multiplication of 2 strings",result1) #this will not print at all

# "4" + "7"
result2 = "4" +"7"
print("this will display 2 strings types, as it will show the 4 and the 7 next to each other, showing",result2)

# '4' * 7
result3 = '4'*7
print("This might result the '4' around 7 times, making it look like this",result3)


# Task 9 - Ask the user for three numbers: a, b, and c. Compute and print the result of a(b+c).
var_a = int(input("enter value for a: "))
var_b = int(input("enter value for b: "))
var_c = int(input("enter value for c: "))

sum = var_a*(var_b+var_c)
print(sum)

'''
# Task 10 - Print the following text exactly: welcome to python class Fall 2025
print("welcome to python class Fall 2025\nI welcome you to my python code")

