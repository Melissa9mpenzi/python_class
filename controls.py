#Through controls, we determine the flow of execution.
#In this, we use conditions like; if, if...else, and if...elif..else
mylist = [20, 40, 30]
if 50 not in mylist:
    print("50 is not in the list mylist")

if 50 in mylist:
    print("50 in the list mylist") 
num = 10
if num >= 10:
    print("The number is equal or greater than 10")
if num < 10:
    pass #if the value of num is less than 10, chill/don't do anything  

#if else
if num % 2 == 0:
    print("num is an even number")
else:
    print("num is an odd number")