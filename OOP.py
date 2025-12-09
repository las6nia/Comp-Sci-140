                                #Object Oriented Programming 
#We use OOP to think of concept to write once and apply for all

#Inventory class - It is not storing chocolate, different departments such as clothing and makeup - others, under inventory
#University - all departments are an instance of the whole university, such as classrooms, 


                                #An object belong to a class
#class - family tree example
#Object - create examples of the class
#Attributes - properties of these object
#Methods - things that are done belonging to that class
'''
class student: #add a colon, replaces curly braces that are done in java
    #Attribute - first set of things
    studentId, firstName, lastName #instance attributes
    def enrollment():
        pass #what does passs do?
    def getHighSchool():
        pass
    def graduation():
        pass

class employee:
    employeeId, employeeName, salary
    def getEmployeeDetails():
        pass
    def

#What is a constructor? a method that constructs a method for the class - in python = init
'''
#bank account
class bankAccount:
    balance = 0 #all 
    customerName = "" #inititalize as no name
    
    def __init__(self, name, bal): #this is how a constructor is built.... self means "look at the current object, in java is 'this'"
       #instance attributes
        self.customerName = name #passing the customer name 
        self.balance = bal
    def deposit(self, amt):
        self.balance+=amt   
                                                #Come back to the bottom code to add limits on free time!!!
    def withdraw(self, amt):
        if (self.balance > amt) and (self.balance-amt != 0): 
            self.balance-=amt
    def getDetails(self): #this is an instance of a method, we do not need to add parameter as it will gather all other details either way
        print(f"Customer {self.customerName} has a balance of {self.balance}") 
    #After every method - compile it so it works
    
acc1 = bankAccount("Luis", 500) #this takes a parameter, and it takes 3 values - this is how an object is created
acc2 = bankAccount("Joe", 3000) #
#How do I call instance method??
print(acc1.getDetails())
print(acc2.getDetails())

#deposit
acc1.deposit(100)
print(acc1.getDetails())

#Joe  - withdraw
acc2.withdraw(2000)
print(acc2.getDetails())
#check this error, joe doesn't have more money
acc2.withdraw(2001)
print(acc2.getDetails())








