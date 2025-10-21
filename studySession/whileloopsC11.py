num = float(input("Enter your first number to add to: "))
totalSum =0 #assign before the loop starts
while num!=0: #Learn - add condition -> while num does not equal 0
    totalSum+=num  #instead of   totalSum = num+num do totalSum+=num to store the value in totalSum - add the new number to whatever totalSum already has
    num = float(input("Enter other numbers to add to: "))
    if totalSum.is_integer():
        totalSum = int(totalSum)

    
print(f"the total sum is: {totalSum:.2f}")
    
