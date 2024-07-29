#Operators are symbols that tell an operant what to do in writing.
a = 20
b = 30
# 20 and 30 are operants
#Arithmetic operators
c = a+b
print(c)
d = b-a
print(d)
e = d*c
print(e)
f = a//b
print(f)
i = b//a
print(i)
j = a/b
print(j)
print(a**2)
print(a%b)
#assignment operators
num1,num2 = 10,5
num3 = 200
num4 = 150
#another assignment operator
num1 += num2 #num1 = num1 + num2 addition operator
print(num1)
num1 -= num2 #num1 = num1 - num2 subtraction operator
print(num1)
num1 *= num2 #num1 = num1 * num2 multiplication operator
print(num1)
num1 /= num2 #num1 = num1 / num2 division operator
print(num1)
num1 %= num2 #num1 = num1 % num2 modulus operator
print(num1)
num1 **= num2 #num1 = num1 ** num2 exponential operator
print(num1)
#comparison operators
print(num1 == num2) #num1 is equal to num2
print(num1 != num2) #num1 is not equal to num2
print(num1 > num2) #num1 is greater than num2
print(num1 < num2) #num1 is less than num2
print(num1 >= num2) #num1 is greater than or equal to num2
print(num1 <= num2) #num1 is less than or equal to num2
#logical operators
#they are used for decision making i.e true or false
#logical and 
print(True and True)
print(True and False) #for it to be true, both options should be true
print(False and False)
#logical or
print(True or False)
print(True or True)
print(False or False)
#logical not
print(not True)
print(not False)
#membership operator
#here we have "in" and "not in"
name = "Lokoroma Melissa"
print("h" in name)
print("M" in name)
print(" " in name)
print("Osman" not in name)
#identity operator
#here we have "is" and "is not"
