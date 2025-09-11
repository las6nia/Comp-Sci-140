
#turning variables to intergers

value1 = input("Number 1: ")
value2 = input("Number 2: ")
result = (int(value1))+(int(value2))
print(type(result))

#be careful of data types ()



# a = int(input("enter first value: \n"))
# b = int(input("Enter second value: \n"))
# ## cannong multiply a string print(a*b)

# print("The sum of",str(a),"and",str(b),"is",str(a+b))


#assignment
first_name = "Adam"
last_name = "Smith"
age = 40

print("Hey, "+str(first_name),str(last_name)+",","you are",age,"years old")



#FIX - errors
age = input("Enter your age\n")
print("next year you will be"+age+1)



#value turned into string (if not an interger)
num = int(input("enter a number: ")) #hello = error



a = int(input("enter first value: \n"))
b = int(input("Enter second value: \n"))
print(c+a) #c does not exist



#runtime error
a = int(input("enter first value: \n"))
b = int(input("Enter second value: \n"))
print(a/0) #logic error



#value, type, name errors

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

# print("the area of the rectangle is",length+width) #logic error

print(length, width,sep=",") #sep="" to separate

a = int(input("enter first value: \n"))
b = int(input("Enter second value: \n"))
print(a+b,end=",")
print(a*b, end=",")


#task
#a = 3
#b = 2
#take value a and B, and display result is, the sum of 3 and 2 is 5, the subtract of 3 and 2
#is 1, the multiplication of 3 and 2 is 6, the division of 3 and 2 is 1.5

a = 3
b = 2

sum = (a+b)
subtract = (a-b)
multiplication = (a*b)
division = (a/b)

print("the sum of 3 and 2 is",sum)
print("the subtraction of 3 and 2 is",subtract)
print("the multiplication of 3 and 2 is",multiplication)
print("the division of 3 and 2 is ",division)


