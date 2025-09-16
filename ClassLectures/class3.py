#an expression is a combination of values, variables, operators (PEMDAS), functions and literals - literals are number 1, a - characters, "Adam" - string. 
#exponents and any mathematical operations
# math modules and random numbers modules - learning

#variable vs identifier - an identifier identifies something (in any of the classes)
# variable - stores a value to extract, change, and modify by using just the name of it


#Class 3 - arithmethic expressions

a =12
b = 20

division = a//b  #if you use this, you will round from 0.6 to 0
remainder = b%a #context of remainder - 
print(division)
print(remainder)

#binary - hexadecimal, 2^0, 1


import math #you can use 'as m' to shorten the import name

a =2 
b = 5
power = math.pow(b,a)
pi = math.pi

print(power)
print(pi)

a =2 
b = 5
equation = a+b*2
print(equation)
equation = (a+b)*2
print(equation)
#mathematical precedence of operators - https://runestone.academy/ns/books/published/fopp/Conditionals/PrecedenceofOperators.html



#exam
a = 2
b = 5
c = 10
#result = a*b**2 #result is 50, this will be in exam
result = (a+b)*c # = 70
result+=a #70+2, result = result+a = 72
print(result)




                            #TASK
#Convert the temperature from celcius to farenheit using the formula 
#F = C*95+32
#take input from the user for celcius temperature
import time

c_temp = int(input("Enter your temperature (Celcius): "))

f_temp = (c_temp*9)/5+32
print("your temperature in Farenheit is: ",f_temp)

                        #TASK =
#calculate the final price after a discount
#inputs: original price and percentage of discount
                    
                    #PRACTICE!!!!#
original_price = int(input("Enter your price: "))
percentage = int(input("Your savings in percent: "))

discount = percentage/100 #this will turn input to .%

amount_saved = original_price * discount #this will multiply the input price times percentage
#this will equal 20
price = (original_price - amount_saved) #This will subtract the original price - the percentage amount
#this  will subtract 200- 20 = 180

discount = discount*100 #Optional - I turned discount (.1) to 10 so it shows to the user

print("You are saving:$",price, ",and your discount was: ",discount,"%")

#Instructor note: 200 -10% -10% which equals 180











