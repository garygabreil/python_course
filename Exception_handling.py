#Error Vs Exception
#Error - indicates problem in the program structure or environment, Errors always lead to application to crash
#if: SyntaxError
#for i in range(10,20): --> Indendation Error
#if
#print("hello" --> Syntax

#Exception --> are a types of errors which can be handled during runtime and prevent crashing
#How to achieve exception handling by, try, except, finally, else

#print(20/0)

# try:
#     result = 20/0
# except ZeroDivisionError:
#     #handle specific exception
#     print("you can't divide by zero!")


value="abc"
print(type(value))


try:
    number=int(value)
except:
    print("something went wrong")

