# Set initial balance
account_balance = 1000.00  
# Display welcome message and balance
print("=== Welcome to the ATM ===")
print(f"Your current balance is: ${account_balance:.2f}")

# Ask user for withdrawal amount
try:
    withdrawal_amount = float(input("Enter the amount to withdraw: $"))

    # Check if the withdrawal is possible
    if withdrawal_amount <= 0:
        print("Withdrawal amount must be greater than 0.")
    elif withdrawal_amount > account_balance:
        print("Insufficient balance. Transaction declined.")
    else:
        account_balance -= withdrawal_amount
        print(f"Withdrawal successful. New balance: ${account_balance:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

print("Thank you for using the ATM!")
