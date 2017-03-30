"""
You have deposited a specific amount of dollars into your bank 
    account (d). Each year your balance increases at the same growth 
    rate (r). Find out how long it would take for your balance to 
    pass a specific threshold (t) with the assumption that you don't 
    make any additional deposits.
"""
def depositProfit(d, r, t):
    y = 0
    while d < t:
        y += 1
        d = d * (1+ r/100)
    return y