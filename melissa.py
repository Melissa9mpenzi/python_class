#if statements
e = 25
d = 44
if d > e:
    print("d is greater than e")
#if there was no indentation when printing, an error would be the outcome in the console/terminal.
#if statements are used for the program to know whether to execute a code or not. i.e in this case, we know that 44 is greater than 25 so we ask the code to print the value as d is greater than e. If it was false, it would not be shown in the terminal.

#elif
#This is mainly used to print results tgat were false in the first option. It's python's way of saying if this isn't right, try this. i.e;
a = 30
b = 30
if b < a:
    print("b is less than a") # this will not show in the console because it is a false if statement.

elif a == b:
    print("a and b are equal")#since this condition is true, it'll be printed in the console.

#else
#this is meant to take up any other condition that weren't true in the preceding conditions/statements. For example;
e = 250
f = 100
if f > e:
    print("f is greater than e")
elif f == e:
    print("f and e are equal")
else:
    print("f is less than e")
#the last condition will be printed in the terminal because the first two conditions were false.

#A while loop.
# a while loop is capable of executing a set of statements as long as the condition is true.i.e;
h = 10
while h < 11:
    print(h)
    h += 10
#the code continues to run infinitely if the addition sign isn't added.

#For loop.
#here, we can execute a set of statements one each for every item in the list, tuple, set or dictionary. i.e;
colors = ["pink", "purple", "red", "grey", "maroon"]
for y in colors:
    print(y)
#all the colors are printed separately each in a new line, one after the other.

#A list.
#Lists are used to keep many values in one varaiable. It is a method of data collection in python.
# We use square brackets after the assignment operator in lists. They are ordered, changeable and allow duplicate values as well.
 #List items are indexed i.e the first value from left to right is assigned starting from 0, and from right to left is assigned starting from -1. Example;
mylist = ["apple", "strawberry", "kiwi", "jackfruit", "pineapple"] 
print(mylist) 
# apple is assigned to index 0, strawberry to 1, kiwi to 2...
#Lists can be of any data type i.e strings, boolean, integers or even complex values.

#A tuple.
#This is also ordered and unchangeable and allows duplicate values.
#They store multiple values in a single variable.
#Here, we use parentheses after the assignment operator.
mytuple = ("spongebob", "fancy nancy", "angellina ballerina", "vampirina")
print(mytuple)
#We cannot add or remove items once the tuple has been created. 
#Tuples can be of any data type.


#Sets.
#This is a collection that's unordered, unchangeable and not indexed as well.
#It does not allow duplicate members.
#Sets use curly brackets/braces to store multiple data in one variable.
myset = {"milk", "tea", "hot chocolate", "cappuchino"}
print(myset)
#They are unordered hence one cannot be sure of the order in which they'll appear in the console.


#Dictionary.
#This is a collection that is ordered and changeable but doesn't allow duplicates.
#Stores values in pairs
#We use curly braces her as well. i.e;
capital_cities = {"UG": "Kampala", "KY":"Nairobi", "RW": "Kigali"}
print(capital_cities)
#UG, KY and RW are keys, and Kampala, Nairobi and Kigali are values.

#Dynamic functions.
#They are parametarized functions.
#Their values are assigned when calling the function and can vary/be changed dynamically.
def myfunc(r,m):
    n = r + m
    print(n)
myfunc(25,25)
myfunc(36,62)


#Static functions.
#Unlike dynamic functions, their values are assigned when defining the function and the parentheses left empty when calling the function.i.e;
def myfunc():
    r,m = 55,70
    n = r + m 
    print(n)
myfunc()

 #THE END.   
