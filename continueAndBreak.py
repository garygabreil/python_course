#keywords - continue and break 
#Only applicable on loops(for, while)

#break - Stopping a iteration/loop when a condition a met
for i in range(1,20):
    if i == 11:
        print(i)
        break
    print(i)

#list of peoples
peoples = ["peter", "bob", "mark", "tomas"]
for temp in peoples:
        print(temp)
        if temp == "mark":
            print("Found!", temp)
            break

#continue - Skips the current iteration and continue with next one

print("**********Block for Continue*************")
peoples = ["peter", "bob", "mark", "tomas"]
for temp in peoples:
        if temp == "mark":
            continue
        print(temp)
print("**********Block for Continue*************")


print("**********Block for Continue/Break**************")
numbers =[10,-5,150,20,-1,90]
for num in numbers:
     if num < 0:
          continue #skip negative numbers 
     if num > 100:
          print("Too big numbers, stopping the loop")
          break
     print("Processing: " , num)
print("**********Block for Continue/Break**************")

