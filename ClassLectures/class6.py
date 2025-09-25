''' Calories = ((Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991) x Time / 8.368 
age = float(input(""))
weight = float(input(""))
heartRate = float(input(""))
time = int(input(""))

calories = (float(age * 0.2757) + (weight * 0.03295) + ((heartRate * 1.0781)-(75.4991)) * time) / 8.368


print(f"Calories: {calories:.2f} calories")
#print("Calories: ",calories, "Calories")


#5.0
#1.5
#3.2

# 172.47    361.66     3.50     13.13


# 2.16 to 2.17 Homework - 2.18 and 2.19 is the value
import math
x = float(input(""))
y = float(input(""))
z = float(input(""))
value1 = math.pow(x,z)

value2= math.pow(z,math.pow(x,y))           #X^Y^Z

print(f"{value2:.2f}")
#print(f"{value1:.2f},{value2:.2f} ")
'''

                #TOPIC - RANDOM MODULE -- iteration (when learning )
'''
import random
a = random.randint(1,100)
print(a)
'''

import random
import math
a = random.uniform(1,100)
b = random.uniform(1,100)
c = random.uniform(1,100)

#finish later  + fix!!!!
ac = math.sqrt((a**2)+(b**2))
bc = math.sqr((c**2)+(a**2))

hypotenuse = math.sqrt((a**2)+(b**2))

print(hypotenuse)
