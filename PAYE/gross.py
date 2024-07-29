#gross salary

def calculate_gross_pay(hours_worked, hourly_rate):
    """
    Calculate the gross pay based on hours worked and hourly rate.
    #hours_worked * hourly_rate = average pay 


    Parameters:
    hours_worked (float): The number of hours worked by the employee.
    hourly_rate (float): The rate per hour.

    Returns:
    float: The gross pay.
    """
    gross_pay = hours_worked * hourly_rate
    return gross_pay
