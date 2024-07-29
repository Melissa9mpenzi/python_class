#How to make functions communicate with one another.
def add():
    a,b = 50,75
    c = a + b
    return c

def sub():
    a = 70
    c = add() - a
    #print(c), when this is printed, it gives us a value in the terminal i.e
    print(c)

print(add())
print(sub()) #Function "sub" doesn't expose any value returned like in "add"
sub()

#This is individual assignment
#CREATE A PYTHON SCRIPT AND CALL IT melissa.py, with comments, write code examples of if conditions, a while loop,functions(static and dynamic), for loop, an example of a list, a dictionary, a tuple and a set.

#In python there are two ways we create functions, either in a static or dynamic way or rather use in-built python functions.