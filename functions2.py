#Functions are self-contained block of code
#In python we have two types of functions;
#1.Static function
#2.Dynamic function(parametarized function)
#Function names follow variable syntax.


#Below is an example of a static function.
def pow():
    num1,num2 = 22,34
    Osman = num1 ** num2
    print(Osman)
def pow2(num1,num2):
    Osman = num1 ** num2
    print(Osman)


def sub():
    num1,num2 = 22,34
    num3 = num1 - num2
    print(num3)
 #Below is a dynamic funtion of the function above
def sub2(num1,num2):
    num3 = num1 - num2
    print(num3)

    
def floor_div():
    num1,num2 = 22,34
    num3 = Osman // num2
    print(num3)
def floor_div2(num1,num2):
    num3 = num1 // num2
    print(num3)
pow() # This will not work because functions do not share variables/ they are self #contained.
#All funtions that don't have anything in their parentheses are called static.

pow2(20,30)
pow2(50,60)

sub2(20,30)
sub2(50,60)



