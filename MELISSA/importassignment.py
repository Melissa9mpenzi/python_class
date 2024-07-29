from PAYE.gross import calculate_gross_pay
from PAYE.net_pay import calculate_net_pay

def mypay():
    hours_worked = 120 # example hours
    hourly_rate = 5000   # example rate

    
    # Calculate gross pay
    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)
    print(f"Gross Pay: {gross_pay}")
    
    # Calculate net pay
    net_pay = calculate_net_pay(gross_pay)
    print(f"Net Pay: {net_pay}")

if __name__ == "__mypay__":
    mypay()
