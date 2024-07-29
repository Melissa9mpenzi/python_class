#Object Oriented Programmming
#It's a software programming concept/idea/paradigm that bases on real world objects.
#Objects are gotten from classes.

#BASICS OF OOP.
#It's built upon class, object, attributes, methods
#A method is a group of statements that describes what an object does to itself or to others.
#A CLASS is a blue print(original copy) of an object.
#Use a phrase "is a" to identify a class of an object i.e Uganda is a country. Uganda being the object and country the class.
#An object is an instance/example of a class.
#Classes are indentified in singular i.e; Country, president, city, boy, girl, lake, river etc.

#Attributes are the characteristics of a class and they're implemented by the objects.
#Attributes are identified at a class level.
#Each object can have different attributes of the same object in a class.

#In writing, how do we create classes in python?
#We use a key word "class" i.e 
class Fruit(): #The class names start with CAPITAL LETTERS.
    pass 
#Classes are not defined, they are created.
class Car():
    number_of_tires = 4
    make = "mercedes"
    model = "c200"
    engine_type = "v-type"
    owner = "Melissa"
    def vroom():
        return "The car vrooms gently"

print(Car.make)
print(Car.model)
print(Car.vroom())
#The statements of the methods of a class are called functions

#The return statement is special in a way that it marks the end of code that needs to be printed
#Parentheses in this case are used to indicate that it's a function.

#Method of a car
#Function belonging to a class is called a method.
#Statements are referred to as behaviors.
