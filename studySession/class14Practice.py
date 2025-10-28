num = int(input("Enter a num of repetitions: "))
class xRange():
def 
if num >= 20:
    for x in range(1, num+1):
        for y in range (1, x+1):
            print("x", end=" ")
        print()
    #condition to make this backwards

else:
    for i in range (1,num+1): #this will be the rows
        for j in range (1, i+1): #this will be the column
            print("*", end=" ")
        print()


