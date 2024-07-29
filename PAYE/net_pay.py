#net_pay 

def calculate_net_pay(gross_pay):
    """
    Calculate the net pay after deductions.

    Parameters:
    gross_pay (float): The gross pay of the employee.

    Returns:
    float: The net pay after deducting NSSF and PAYE.
    """
    NSSF_RATE = 0.11
    PAYE_RATE = 0.30

    # Calculate NSSF deduction
    nssf_deduction = gross_pay * NSSF_RATE
    
    # Calculate PAYE deduction
    paye_deduction = gross_pay * PAYE_RATE
    
    # Calculate net pay
    net_pay = gross_pay - nssf_deduction - paye_deduction
    
    return net_pay
