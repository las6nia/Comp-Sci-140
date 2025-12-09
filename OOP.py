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
'''
#Task - create a book class with instance attributes title, author, and price. create an instance method to get details of a book object and chance the price of a book object. Create 3 difference book objects and use the instance methods to display the book information and chance the prices


class book:
    bookPrice = 0
    bookName = ""
    def __init__ (self, book, cost):
        self.bookName = book
        self.bookPrice = cost
    def displayInformation(self, book, cost):
        self.bookName = book
        self.bookPrice = cost
        print(f"The name of this book is {self.bookName} and the price is {self.bookPrice}")
    


#Instructor Version: 
class book2:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price= price
    def getDetails(self):
        return f"Book name: {self.title}, Book Author: {self.author}, Book Price: {self.price}"
    
    def changePrice(self, priceChange):
        self.price = priceChange

myBooks = [] ##teacher went to fast - check picture notes and edit later
b1 = book2("Intro to C++", "Lind L Tailor", 65.30)
b2 = book2("Intro to Python", "Adam James", 129.50)
print(b1.getDetails) #check this 

print(myBooks[0].getDetails()) #Check this later




myBooks[0].author #this will print the author name in ''

#Access modifyer - public - private(no one but you), 
  self.author = __author #this will activate private mode and cannot be access, this will be fixed
#Python does not enforce protected mode
#To show the protected property you would do just 1 underscore as such:
  self.author = _author

#But how can I access in private mode?
#you have to have Getters and set them inside the same classes, you can however acccess by the same classes

#classes, objects, instance, list of objects, access modifiers, 




        







