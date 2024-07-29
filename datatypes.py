#Different data types that we have in python.
num1 = 10 #python will know that the given variable belongs to a particular data type.
#These are the data types we are dealing with;
#numeric
#string
#sequence
#mapping
#boolean
#set
#In numerics, we have integers, float and complex values. 
print(type(num1))
num2 = 10.5
print(type(num2))
name ="Lokoroma Melissa"
print(type(name))
num3 = "10.5"
print(type(num3))
num4 = 1+2j
print(type(num4))
#In sequence data types, we have a list, a tuple and a dictionary.
#A list
languages = ["Python" , "JavaScript" , "C+" , "Java" , "Cp#" , 10 , 20.5]
students = ["Vivian", "Melissa", "Aisha" , "Livia" ,"Jonathan", "Afrah" ,"Edgar"]
print(languages)
print(10 in languages)
print(languages[0]) #we start counting from 0 when starting from left to right
print(students[-1],students[-3]) #we use negative index(starting from -1) when starting from right to left
languages.append("go") #adds the value at the end of the list.
print(languages.pop()) #removes the word go from languages i.e the values in a list can be manipulated
print(languages)
#tuple is like a list but instead uses oval brackets/parentheses instead of square ones. Tuples are immutable. i.e print(item.pop()) will never work out.
item = (10,20,30,40,50,60,180,360)
print(item[-3])
print(item[2])
#Mapping datatypes; dictionary/dict:
#dictionary type we use braces {}
presidents = {"UG":"Yoweri Kaguta","KY":"Ruto William","RW":"Paul Kagame","TZ":"Samia Hassan"}
print(presidents["UG"])
print(presidents.keys())
print(presidents.values())
# A SET
#A set stores unordered list of unique items.
student_id = {112, 112, 114,115,117,116}
print(student_id)
#Pair assignment
#Declare a list/variable called "puzzle" 
puzzle = [20,50,[30,40,[50,[100]]]]
#Discuss how to access 100 and print it out.

print(puzzle[2][2][1][0])
print(puzzle[-1][-1][-1][-1])

#A statement that evaluates to something is called an expression.
amount = puzzle[0] + puzzle[1]
print(amount)