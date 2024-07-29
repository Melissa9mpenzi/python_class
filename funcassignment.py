#Assignment; WRITE A DYNAMIC FUNCTION THAT TAKES ON THE GROSS SALARY OF AN EMPLOYEE AND CALCULATES HIS PAYE AND NSSF AND PRINTS OUT THE NET PAY. 
#Net pay is calculated after the deduction of 11%(0.11) of NSSF and 30%(0.3) of PAYE.
#Use relevant variable names when defining functions i.e if creating a name for net pay, you can use def net_pay():



def calculated_net_pay(gross_salary):
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

# Example:
gross_salary = 2000000
net_pay = calculated_net_pay(gross_salary)

gross_salary = 5500000
net_pay = calculated_net_pay(gross_salary)