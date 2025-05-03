#public
#syntax: variable_name
#Access: Accessible from anywhere(inside and outside the class)
#Defualt: All class member are public by default

class Animal:
    def __init__(self):
        self.animal_name="tiger"

an = Animal()
print(an.animal_name)

#protected
#syntax: _variable_name (single underscore prefix)
#Access: Indicate that the variable/method is only used internal purpose, but still accessible outside the class


class Animal:
    def __init__(self):
        self._animal_name="tiger" #protected varibale
    def _sum_of_():
        print("sum")
an = Animal()
print(an._animal_name) #Accessible but not recommended


#private 
#syntax: __variable_name (double underscore prefix)
#Access: Indicate that the variable/method is only used internal purpose, but still accessible outside the class

class Animal:
    def __init__(self):
        self.__animal_name="tiger" #private varibale
an = Animal()
print(an.__animal_name) #Attribute error
