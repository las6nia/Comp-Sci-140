print("Rudy\\\nMaya\\nJoe\nJen")
print(r"Tab escape sequence: \t")

# Assign wall_area with a float read from input
wall_area = float(input())

# Compute num_gallons
num_gallons = wall_area / 350.0

num_gallons = f"{num_gallons:.5f}"

print(num_gallons)
# kinetic energy one challenge
object_mass = float(input())
object_velocity = float(input())

kinetic_energy = (1.0/2.0) * object_mass * (object_velocity**2)

print(f"Kinetic energy is {kinetic_energy:.4f}")

# minutes to hours.             idea!!! make an app that tells you what time you would like to go to sleep, how long you would be sleeping for
#and at what time you would be waking up at, also how much time you have left 
minutes = int(input("Enter minutes: "))
hours = minutes // 60
minutes_remaining = minutes % 60

print(minutes, "minute(s) is", hours, "hour(s) and", minutes_remaining, "minute(s).")

#STUDY THIS -  MODULOS??????

#2)Given a non-negative number x, which expression has the range -10 to 10?
x = 0 #not added 2.7 zybooks!
x % -10

(x % 21) - 10

(x % 20) - 10

#remainder and conversion of years!!

total_years = int(input())

num_centuries = total_years // 100 
num_decades = (total_years %  100 )//10
num_years = total_years % 10

print("Centuries:", num_centuries)
print("Decades:", num_decades)
print("Years:", num_years)

#importing modules - 2.8, styudy how to attach documents
#it says it can be done having the same document and using import (filename) and can be used using the properties of the variables, for example - 
            # import names - other file
            # print(names.last) - from names
# The pet_names.py module

print ("Initializing pet variables...")
pet_name1 = "Ryder"
pet_name2 = "Jess"
pet_weight1 = 5.1
pet_weight2 = 8.5

# Executes only if file run as a script (e.g., python pet_names.py)
if __name__ == "__main__":
    print("Pet 1:", pet_name1, "was born", pet_weight1, "lbs")
    print("Pet 2:", pet_name2, "was born", pet_weight2, "lbs")
# A script favorite_pet.py that imports and uses the pet_names module.

import pet_names  # Importing the module executes the module contents  

print("My favorite pet is", pet_names.pet_name1, "-")
print("I remember when he weighed only", pet_names.pet_weight1, "pounds.")
print("I love", pet_names.pet_name2, "too, of course.")

#random module 
# Returns a random integer between 12 and 19 inclusive
print(random.randrange(12, 20))

# Returns a random integer between 12 and 20 inclusive
print(random.randint(12, 20))

#random.ranrange(2,10) will print from from 2 to 9
#random.randint(2,10) will print from 2 to 10

            #study random.randrange, random.randint


            #study common scape sequences!
            #study backlash, single quote, double quote(\")m \n new line, \t tab
    
    
            #STUDY APPENDS, TUPLES, AND LIBRARIES

             #  TASK - DIVIDE 3 TIMES AND PRINT THE 3 OUTPUTS 2.16 LAB
user_num = int(input())
div_num = int(input())

division1 = int(user_num // div_num)
division2 = int((division1/1)/div_num)
divison3 = int(division2 / div_num)
print(division1, division2, divison3)



'''
Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.

'''

# Read the full name
#
fullName = input("Enter full name: ")

nameParts = fullName.split()

firstName = nameParts[0]
lastName = nameParts[-1]


output = lastName + ", " + firstName[0] + "."

if len(nameParts) == 3:
    middleName = nameParts[1]
    output = lastName + ", " + firstName[0] + "." + middleName[0] + "."

print(output)

