Enter_amount = int(input("Enter the amount you want to withdraw: "))
if Enter_amount > 10000:
    Total_Amount = (Enter_amount * 0.1) + Enter_amount
    print(f"Your total amount is: {Total_Amount} and therefore you have been awarded an addition of 10%")
elif Enter_amount > 5000:
    Total_Amount = (Enter_amount * 0.05) + Enter_amount
    print(f"Your total amount is: {Total_Amount} and you have been awarded an addition of 5%")
else:
    print(f"Your total amount is: {Enter_amount} therefore no addition is awarded")