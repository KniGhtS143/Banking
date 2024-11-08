accounts = {}

# Generate a unique account number (starting from 1)
account_counter = 1

while True:
    # Display the menu
    print("\n=== Banking System Menu ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    
    # Get user's choice
    choice = input("Enter your choice: ")
    
    if choice == '1':
        # Create Account
        name = input("Enter your name: ")
        # Account number is generated using the current value of account_counter
        account_number = account_counter
        account_counter += 1  # Increment the counter for the next account
        # Initialize the balance as 0.0
        accounts[account_number] = {'name': name, 'balance': 0.0}
        print(f"Account created successfully! Your account number is {account_number}")
    
    elif choice == '2':
        # Deposit Money
        try:
            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                deposit_amount = float(input("Enter the amount to deposit: "))
                if deposit_amount > 0:
                    accounts[account_number]['balance'] += deposit_amount
                    print(f"{deposit_amount} deposited successfully! New balance: {accounts[account_number]['balance']}")
                else:
                    print("Deposit amount must be greater than 0.")
            else:
                print("Account does not exist.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif choice == '3':
        # Withdraw Money
        try:
            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount > 0:
                    if accounts[account_number]['balance'] >= withdraw_amount:
                        accounts[account_number]['balance'] -= withdraw_amount
                        print(f"{withdraw_amount} withdrawn successfully! New balance: {accounts[account_number]['balance']}")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Withdrawal amount must be greater than 0.")
            else:
                print("Account does not exist.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif choice == '4':
        # Check Balance
        try:
            account_number = int(input("Enter your account number: "))
            if account_number in accounts:
                print(f"Your current balance is: {accounts[account_number]['balance']}")
            else:
                print("Account does not exist.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif choice == '5':
        print("Exiting the banking system.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")