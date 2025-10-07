#new class
grade = int(input("Enter your grade: "))

if grade > 89:
    print("A")
elif grade >75 and grade <= 89:
    print("B")
elif grade > 59 and grade <=75:
    print("C")
else:
    print("F")

grade2 = int(input("enter you grade (method 2): "))

if grade2 < 60:
    print("F")
elif grade < 75:
    print("C")
elif grade < 90:
    print("B")
else:
    print("A")
    
grade3 = int(input("enter you grade (method 3): "))
if grade3 >= 90:
    print("A")
elif grade3 >=80:
    print("B")
elif grade3 >= 70:
    print("C")
else:
    print("F")
'''
# you are also able to enclose the conditions withing an if and continue with an if
                #example above: 
if (age >= 0 and age >= 100):
    if age >= 90:
        print("A")
    elif age >= 80:
         print("B")
    else: 
        print("exit")
'''
