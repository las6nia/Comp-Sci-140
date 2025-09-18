'''

p = "Pa"; p2 = "PA"; p3 = "Pa"
#all are based in ascii value
#if all variables are the same but the values are different (in ASCII VALUE), the equation will print the highest value in ASCII 
#the bigger letter 
result = p>p2
print(result)
                        IN EXAM!!


# and, or , not values
# OR

#not - becomes true/false, if this is not 1, it's 0

#a =1 or b = 0 == true

a=True; b = False ; c = False; d = True

a,b,c,d = True, False, False, True

#and or not

a,bv
#study/practice




a =15
b = 20
c = a<b #IN QUIZ, evaule this equation (what type it will print)
print(bool(a or b))
print('p' or 'P') #True, this 2 statements will print both results


#receipt value print task
import math as math
name = 'Alice'
age = 25

print(f"the value of pie is: {math.pi:.2f}")#FORMAT - :.#ofdecimalsf
print(f"The percentage of 87 is: {87/100:.1%}")
print(f"Hello, {name}, next year you will be {age+1} years old")

population = 123456789
print(f"population is {population:,}") #large numbers = :, 


storeName = "Walmart"
print(f"|{storeName:^20}|") #center
print(f"|{storeName:<20}|")  #left
print(f"|{storeName:>20}|")  #right


number = 42
print(f"Number with leading zeros {number:05}")

print(f"I need to print curly braces {{}}")

name 
age = 20
city = "Green Bay"

# message = f"#Hello {name}!:
#you are {age} years old
#you live in {city}".   change to ''3
print(message)


value = 253645
print(f"Scientific representation is: {value:e}")
'''
student1 = 'Alice'
grade1 = 40

student2 = 'Bob'
grade2 = 20

student3 = 'Charlie'
grade3 = 25

print(f'{'STUDENTSCORE:':^20}')
print("-"*20)
print(f"{"Score: ":<5} {"Name: ":>9}")

print(f"{grade1:<5} {student1:>9}")
print(f"{grade2:<5} {student2:>9}")
print(f"{grade3:<5} {student3:>9}")


