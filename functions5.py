#In-built functions.
name = input("Please enter your name: ")
print("You are welcome! " , name)
#By default, input function takes on strings.
#Input function is a python in-built function that reads values from the keyboard and takes on those values as  strings by default.

age = float(input("Please enter your age: "))
print("This is my age: " , age)
print(type(age))

def check_even(num):
    if num % 2 == 0:
        print(num)
    else:
        print("The number is odd")
mynum = int(input("Please enter your number here: "))

check_even(mynum)

#Assignment; WRITE A DYNAMIC FUNCTION THAT TAKES ON THE GROSS SALARY OF AN EMPLOYEE AND CALCULATES HIS PAYE AND NSSF AND PRINTS OUT THE NET PAY. 
#Net pay is calculated after the deduction of 11%(0.11) of NSSF and 30%(0.3) of PAYE.
#Use relevant variable names when defining functions i.e if creating a name for net pay, you can use def net_pay():



def calculate_net_pay(gross_salary):
    #Rates for deductions;
    NSSF_RATE = 0.11
    PAYE_RATE = 0.3
    
    #NSSF deduction
    nssf_deduction = gross_salary * NSSF_RATE
    
    #PAYE deduction (after NSSF deduction)
    paye_deduction = (gross_salary - nssf_deduction) * PAYE_RATE
    
    #Calculating net pay;
    net_pay = gross_salary - nssf_deduction - paye_deduction
    
    # Print the details
    print(f"Gross Salary: {gross_salary}")
    print(f"NSSF Deduction (11%): {nssf_deduction}")
    print(f"PAYE Deduction (30% of (Gross Salary - NSSF Deduction)): {paye_deduction}")
    print(f"Net Pay: {net_pay}")

    return net_pay

# Example usage:
gross_salary = 5000  # Example gross salary
net_pay = calculate_net_pay(gross_salary)

#A return statement is used to show a value outside of that function.
#Range is a function which returns something (helps you to get values within a given range).
