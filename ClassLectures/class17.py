'''
x = 10
def outer():
    x = 20
    def inner():
        x = 50
        print(x) #these will never print as the function is never called (you can do a function inside a function)
        #If you change the indentation of this code you will be able to  call the outer function going outside of the inner function
    inner() #play with inner and outer indentations
outer()

#   -   -   -   -   -   -   -       -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
# Y is 
x = 10
def outer():
    y = 20
    def inner():
        y = 50
        print(y)
    inner() #the inner function is dependent on the outer
    print(y)
outer()
#It will be taking the first as it was the last one (study stack meaning on these functions)


#   -   -   -   -   -   -   -       -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

def area(radius):
    Returns the area of a circle
    Parameters is radius
    datatype: decimals
    
    return (3.14 * radius * radius)
#help(area) - see documentation about this function

def greet(name):
    print(f"Hello, {name}!")
myfunc = greet
myfunc("John")



def twoLevelFunction(a, func):
    print(func)


def secondNum():
    return int(input("Enter the second number: "))
f = secondNum
twoLevelFunction (3 + secondNum()) #printing an object that then goes into a variable

'''


""" Read in first equation, ax + by = c """
a = int(input())
b = int(input())
c = int(input())

""" Read in second equation, dx + ey = f """
d = int(input())
e = int(input())
f = int(input())

""" Type your code here. """
found = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            found = True

if not found:
    print("No solution")


