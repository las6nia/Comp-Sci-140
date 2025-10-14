'''
temperature =  int(input("Enter the temperature: "))
humidity =  int(input("Enter the humidity: "))
rainfall =  int(input("Enter the rainfall: "))      #might have to change into a float

if (temperature >30 and humidity >70 and rainfall <5):
    print("Heatwave advisory")
elif (temperature > 30 and humidity >70):
    print("Heatwave")
elif (rainfall > 5):
    print("rainfall")
else:
    print("normal condition")


#get problem pictures from phone

num = int(input("Enter number: "))
if num > 0:
    print("Positive")
    if num % 5 == 0:
        print("Multiple of 5")
        if num % 2 == 0:
            print("Divisible by 2 - even")
        else:
            if(num < 0 ):
                print("your number is negative, and multiple of 5")
            else: 
                print("it's 0")
else:
    if (num < 0 ):
        print("Your number is negative ")
    else:
        print("Your number is 0")
'''
#Order of operations from left to right in python, 3.10.1 in Zybooks
x = 7
y = 6
z = 3

result = y*z<x-1 or z ==3
print(result)
