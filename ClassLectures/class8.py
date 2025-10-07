'''
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

# you are also able to enclose the conditions withing an if and continue with an if
                #example above: 
if (age >= 0 and age >= 100):
    if age >= 90:
        print("A")
    elif age >= 80:
         print("B")
    else: 
        print("exit")


#enter the input of the BMI between 10-50. If the BMI is less than 18.5 print("underweight"), if bmi <18.5= bmi <25 (26): print("normal")
#else print overweight 
bmi = float(input("enter your BMI: "))

if bmi >= 10.0 and bmi <=50.0:
    if bmi < 18.5:
        print("underweight")
    elif bmi >=18.5 and bmi <= 25.0:
        print("Normal")
    else:
        print("Overweight")
    
else:
    print("enter a valid number")
'''
grade = int(input("enter your grade as interger: "))
attendance= int(input("Enter your attendance percentage: "))

if (grade > 59 and attendance > 74) and (grade < 101 and attendance < 101):
    if grade >= 60 and attendance > 74:
        print(f"you failed the class with a score of {grade} which is an D but attendance of %{attendance}!")
    elif grade >= 70 and grade <= 75 and attendance > 74:
         print(f"you passed the class with a score of {grade} which is an C and attendance of %{attendance}!")
    elif grade >= 80 and grade <=89 attendance > 74:
         print(f"Congrats! You passed the class with a score of {grade} which is an B and attendance of %{attendance}!")
    else:
        print(f"Congrats! You passed the class with a score of {grade} which is an A and attendance of %{attendance}!")
elif grade > 59 and attendance <75:
    print(f"Failed. You have a really good grade of {grade} but did not pass the class as you have a %{attendance} of your attendance ")
else:
    print("Invalid Syntax")
