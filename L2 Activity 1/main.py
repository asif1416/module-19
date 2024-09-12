# Tip the waiter
def total_calc(bill_amount, tip_perc):
    total = bill_amount*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"please pay ${total}")
bill_amount = int(input('Enter the bill amount you want to pay: '))
tip_amount = int(input('Enter the tip for the waiter: '))

total_calc(bill_amount, tip_amount)
