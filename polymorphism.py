#polymorphism - many forms
#applicable only METHODS

# class Student:
#     def name(self):
#         print("Student: this is method")

# class Teacher:
#      def name(self):
#         print("Teacher: this is method")

# stud = Teacher()
# stud.name()


#Type-1
#Duck typing (Pythonic programming)
#If it walk like a duck and quacks like a duck, it's duck

class Duck:
    def quack(self):
        print("Quack quack")

class Human:
     def quack(self):
        print("It's a human")

def call_quacks(objc): #methods
    objc.quack()

call_quacks(Duck())
call_quacks(Human())


#payment
#cash, upi, debit-card, credit-card

class cashPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "via cash")

class upiPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "via UPI")

class debitCardPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "via debit-card")

class creditCardPayment:
    def pay(self, amount):
        print("Paid Rs.", amount, "via credit-card")

#common methods
def process_payment(payment_method, amount):
    payment_method.pay(amount)

pay_mode = "credit"
if pay_mode == "cash":
    output = cashPayment()
elif pay_mode == "upi":
    output = upiPayment()
elif pay_mode == "debit":
    output = debitCardPayment()
elif pay_mode == "credit":
    output = creditCardPayment()
else:
    raise Exception("unsupported payment method")

process_payment(output, 1000)


#Type 2
#Operator Overloading, +,-,/,*,
print("Sum of two number:", 10 * 10)
print("Sum of two number:", int.__mul__(10,10))


#Type 3
#Methods Overloading 
class Student:
    sum = 0
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            sum = a + b + c
        elif a!=None and b!=None:
            sum = a + b
        else:
            sum = a 
        return sum
    
s1 = Student()
print(s1.add(10,30,20))

#Type 4
#Method Overriding
class Human:
    def walk(self):
        print("Humans can walk")
        
class Jonny(Human):
    def walk(self):
        print("Jonny can walk")
a = Jonny()
a.walk()

    


