'''
import psutil
process = psutil.Process()
print(process.memory_info().rss)  # in bytes 

item1 = "Apples"
price1 = 1.31
quantity1 = 2.3


item2 = "orange"
price2 = 3.52
quantity2 = 1.6

item3 = "grapes"
price3 = 2.59
quantity3 = 0.59

print(f"{'Shopping receipt':^40}")
print("-"*40)
print(f"{'Item':<15}{'Qty':>5}{'Unit Price':>12}{'Total':>8}")
print("-"*40)

total1 = price1*quantity1
total2 = price2*quantity2
total3 = price3*quantity3
print(f"{item1:<15}{quantity1:>5}{price1:>12.2f}{total1:>8.2f}")
print(f"{item2:<15}{quantity2:>5}{price2:>12.2f}{total2:>8.2f}")
print(f"{item3:<15}{quantity3:>5}{price3:>12.2f}{total3:>8.2f}")
print("-"*40)
print(f"{'Grand Total':<32}{total1+total2+total3:8.2f}")


                    TASK!!!

name1 = "Alice"
math1 = 85
science1 = 92
english1 = 78
total1 = math1+science1 + english1
average1 = total1/3

name2 = "Bob"
math2 = 76
science2 = 81
english2 = 90
total2 = math2+science2+ english2
average2 = total2/3


name3 = "Charlie"
math3 = 90
science3 = 88
english3 = 95
total3 = math3+science3+ english3
average3 = total3/3


report = "STUDENT MARKS REPORT"
print(f"{report:^60}")
print("-"*60)
print(f"{'Name':<15}{'Math':>5}{'Science':>12}{'English':>9}{'Total':>9}{'Average':>10}")

print(f"{name1:<15}{math1:>5}{science1:>11}{english1:>9}{total1:>9}{average1:>10.2f}")
print(f"{name2:<15}{math2:>5}{science2:>11}{english2:>9}{total2:>9}{average2:>10.2f}")
print(f"{name3:<15}{math3:>5}{science3:>11}{english3:>9}{total3:>9}{average3:>10.2f}")

classAverage = (average1 + average2 + average3)/3
print("-"*60)

print(f"{"Class Average":<32}{classAverage:>27.2f}")
print(f"{'END OF REPORT':^60}")



#lecture 5
#print(r"this is a /t and \t testing") - use this to use

normal_strings = ("C:\\users\\users\\alice\\documents")
print(normal_strings)

raw_string = r"C:\\users\\users\\alice\\documents"
print(raw_string)


import re
pattern = r"\d{3}-\d{2}-\d{4}"
#print(pattern) - see the pattern that it prints
text = "My SSN is 123-45-6789"
match= re.search(pattern,text)
print(match.group())

#print(r"C:\\users\\users\\alice\\documents"+"\\")  class problem = be able to add \ at the end of the directory


#if you try to use a raw string and type \ at the end it will be an error
#raw_string = r"hello worldss\"


normalPath = "Normal Path: C: \n"
ewFolder = "ewfolder \test \n"
rawPath = r"Raw Path:" + "C:\\ewfolder\\test"
print(normalPath,ewFolder,rawPath)
'''
                    #class work 3- class 5
import math as math
x2 = int(input("Enter value for X1: "))
x1 = int(input("Enter value for X2: "))

y2 = int(input("Enter value for Y1: "))
y1 = int(input("Enter value for Y2: "))

calculation= math.pow(x2-x1 ,2) + math.pow(y2-y1 , 2)
sqr = math.sqrt(calculation)

print(f"{sqr:.2f}")

#this is without using import math

X2 = int(input("Enter value for X1: "))
X1 = int(input("Enter value for X2: "))

Y2 = int(input("Enter value for Y1: "))
Y1 = int(input("Enter value for Y2: "))

calculation2= (X2-X1)**2 + (Y2-Y1)**2
sqr2 = (calculation2) ** 0.5
print(f"{sqr2:.2f}")


