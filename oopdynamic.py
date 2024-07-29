#HOW TO A CREATE DYNAMIC CLASS:

#we create a constructor.
#special function(method) "__init__" to get the values of the individual fruits. This function is called shishi.
#In the shishi method, you start with the word "self" followed by the values of the object.
#"Self" is used to identify the property/ charateristics/ the attributes/ the features of the class.i.e self.name is the property of the class. You can use any other word in place of self as long as it's used correctly like how self was used in this case.

#a constructor is a special method we use to initialize an instanciated object
class Fruit:
    def __init__(self,name,weight,color,size,price,owner):
        self.name = name
        self.weight = weight
        self.color = color
        self.size = size
        self.price = price
        self.owner = owner

Fruit1 = Fruit("apple", "200gms", "green", "big", "1000shs", "Melissa")
Fruit2 = Fruit("grape", "50gms","purple", "small", "200shs", "Enzo")
Fruit3 = Fruit("watermelon", "2kgs", "green", "big", "4000shs", "Vee")
print(Fruit1.name)
print(Fruit1.weight)
print(Fruit1.color)
print(Fruit1.price) # when including the currency, you put the integers in strings alongside the currency i.e shillings.
print(Fruit1.owner)
print(Fruit3.weight)


#python is modular which means python can be used to perform different functionalities in different fields