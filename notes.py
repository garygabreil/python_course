#Constructor --> 
# def MyName(): -Method or Function

#constructor is also special method, method name which same name as a class, it's called constructor
#what the use of it?


#function - to create funtion in python, it's should have keyword "def"
#syntax: def <function_name>(self):

# class
class Animal:
    # default constructor
    #def __init__(self):
    def __init__(self,m1,m2):
        self._t1 = m1
        self._t2 = m2
        print("Sum of two number :", self._t1 + self._t2)
        
    # method
    def tiger(self):
        # print statement
        print("Lives in the forest")

#a1 = Animal() #constructor, to instanitaiated a object- (correct)
a1 = Animal(10,20) #when passing arguments into a constructor it's called as parameterized constructor, to instanitaiated a object- (correct)
a1.tiger() #calling a method

#mongodb - nosql based database 
#ticketing tool
#no.of ticket, status -in-progress, completed
#class statsReport:
    #def __init(self):
        #connection strings of mongo
    #def getStatus:
        #logic


