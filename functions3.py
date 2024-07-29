def myfunc():
    a,b = 100,50
    c = a + b
    print(c)

#I'm calling the function above
myfunc()
myfunc()
myfunc()
#In lines 7,8 and 9, we're invoking the function "myfunc"
#A function is defined not created or made.
#The body of the function(lines 2,3 and 4) is called the function definition.

#Dynamic function
def myfunc2(a,b):
    c = a + b
    print(c)

#I'm invoking the function above
myfunc2(45,60)
myfunc2(70,25)
myfunc2(80,20)
#We deal with arguments and parameters when calling dynamic functions.
#Arguments are values for the parameters such as 45,60 and 70,25 in this case.

def names(name):
    for x in name:
        print(x)

our_names = ["Melissa", "Tracy", "Vivian", "Joy", "Afrah"]

names(our_names)

def odd(x):
    for num in range(x):
        if num % 2 != 0:
            print(num)
odd(20)

def even(x):
    for num in range(x):
        if num % 2 == 0:
            print(num)
even(20)
