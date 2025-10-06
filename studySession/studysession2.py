'''#Practice problems found by using chat gpt
#1 - Even or Odd – Ask for a number and print whether it’s even or odd.

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"your number is even\nYour number: {number}")
else:
    print(f"your number is odd\nYour number: {number}")


#2 - FizzBuzz – Print numbers 1–100, but replace multiples of 3 with "Fizz", multiples of 5 with "Buzz", and both with "FizzBuzz".
import random

generate = int(input("number: "))



if generate %3 == 0 and generate % 5 == 0:
    print("FizzBuzz")
elif generate %3 ==0 and not generate % 5 ==0:
    print("Fizz")
else:
    print("buzz")
print(f"The number was {generate}")

#3 - Temperature Converter – Convert Fahrenheit ↔ Celsius.

fahrenheit = float(input("Enter your temperature in Fahrenheit: "))

celcius = (fahrenheit - 32) * 5/9

print(f"Your Farenheit temperature is: {fahrenheit:.2f}\nYour Celcius temperature is: {celcius:.2f}")


#Simple Calculator

number1= int(input("Enter first num: "))
number2= int(input("Enter second num: "))
operator = str(input("Enter your desired operator - '+', '-', '*','/' : "))
if operator == '+':
    print(number1 + number2)
    
elif operator == '-':
    print(number1 - number2)
    
elif operator == '*':
    print(number1 * number2)
    
elif operator == '/':
    print(number1 / number2)
         
else:
    print("Enter a valid number")
'''
        
