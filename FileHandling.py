
#file handling is manipuation of files csv,excel,txt,json etc
#modes
# r - read
# w - write
# a - append
# x - create of file
# b - binary mode
# t - text mode(default mode)

# syntaxt : 
# with open("<file_path>","<mode>") as file:

#read
with open("/Users/garygabreil/Documents/development/nifi/test.txt","r") as file:
    content = file.readlines()
    print(content)


#write
with open("/Users/garygabreil/Documents/development/nifi/test.txt", "w") as file:
   content = file.write("I'm writing a new line into this file")
   print(content)


#append   
with open("/Users/garygabreil/Documents/development/nifi/test.txt", "a") as file:
    content=file.write("\n this is a new line to be appended")
    print("appened content -- ", content)

with open("/Users/garygabreil/Documents/development/nifi/test.txt", "a") as file:
    content=file.write("\n third line to be appended")
    print("appened content -- ", content)
