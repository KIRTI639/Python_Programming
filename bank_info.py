# Write a program that has following menu:
# Enter code w for withdraw.
# Enter code d for deposit.
# Enter code c for checking balance.

# Note: 1 take initial amount as input from user.

# Note:2 You can withdraw an amount only if balance is greater than or equal to 500 and withdrawing amount should be less than balance.
Total_balance = int(input("Enter the total amount :"))
money_want = int(input("Enter the amount you wanted to withdraw."))
if Total_balance>=500 and money_want < Total_balance:
    withdraw = Total_balance - money_want
    print(f"Now Remaining amount is {withdraw}.")
    

