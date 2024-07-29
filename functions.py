#A group of code doing a specific task and is given a name is called a function.
#Functions can be "defined" by developers and others are already defined in python.
num1,num2 = 20,30
num3 = num1 + num2
print(num3)
#Turning the above into a function
def sum():
    num1,num2 = 20,30
    num3 = num1 + num2
    print(num3)

#Calling a function sum
#We call a function by its name and the parentheses
sum()

#semantics is the meaning of what you've written.

def div():
    num1,num2 = 22,34
    num3 = num1 / num2
    print(num3)

def mod():
    num1,num2 = 20,30
    num3 = num1 % num2
    print(num3)

def multiple():
    num1,num2 = 22,34
    num3 = num1 * num2
    print(num3)

def pow():
    num1,num2 = 22,34
    num3 = num1 ** num2
    print(num3)

def sub():
    num1,num2 = 22,34
    num3 = num1 - num2
    print(num3)

def add():
    num1,num2 = 22,34
    num3 = num1 + num2
    print(num3)
    
def floor_div():
    num1,num2 = 22,34
    num3 = num1 // num2
    print(num3)