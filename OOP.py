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
        self.customerName = name #passing the customer name 
        self.balance = bal


