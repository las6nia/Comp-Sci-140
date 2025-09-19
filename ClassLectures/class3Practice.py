                    ######CHAT GPT GENERATED PROBLEMS#####
#1 - Write a program that asks the user for their name and age, then prints a message saying how old they will be in 5 years.
'''
mainAge = int(input("Enter your age: "))
mainAge = mainAge + 5 
print(f"You will be {mainAge} in 5 years!")
'''

#2 - Write a program that takes a number from the user and prints its multiplication table from 1 to 10.
'''
mainNumber = int(input("Multiplication table(to 10) for:  "))

for i in range(10):

        result = mainNumber * (i)
        i = i +1
        print(f"{mainNumber} X {i} is:",(result + mainNumber)) #pretty sure there's a better way
        # I do not plan on seeing any ways to shorten it / any chat GPT
    '''
'''
#3 - Write a program that asks the user for three numbers and prints the largest one.

number_a = int(input("enter first number: "))
number_b = int(input("enter second number: "))
number_c = int(input("enter a third number: "))
#most efficient
max_Numbers = max(number_a,number_b,number_c)

if number_a == number_b == number_c:
    print("All numbers are the same :)")
else:
    print(f"The max number is {max_Numbers} ")

'''

'''
#second solution = 
numbers = (number_a,number_b,number_c)
if (number_a > number_b and number_a > number_c):
    print(f"largest number: {number_a}")

elif (number_b> number_a and number_b > number_c):
    print(f"largest number: {number_b}")

elif (number_c > number_a and number_c > number_b):
    print(f"largest number: {number_c}")

else:
    print("All numbers are the same :)")

#First solution - 

numbers = [number_a,number_b,number_c]
same = (number_a == number_b == number_c)

if (number_a>=numbers[1,2]):
    print(f"largest number: {number_a}")
elif (number_b>=numbers[0,2]):
    print(f"largest number: {number_a}")
elif (number_c>=numbers[0,1]):
    print(f"largest number: {number_c}")
else:
    print("All numbers are the same :)")
'''

                    #LeetCode style question (to practice)
#Problem: Second Largest Number Given a list of integers, return the second largest number in the list. If the list has fewer than 2 distinct numbers, return None.

numList = [2,7,11,15,14]

largestNumber = max(numList)

smallestNumber = min(numList)

if (smallestNumber == largestNumber):
    print("none")
    
