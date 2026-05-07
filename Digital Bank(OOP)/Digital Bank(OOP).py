class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted")
        self.show_balance()

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted")
        else:
            print("Error: Not enough balance!")
        self.show_balance()

    def show_balance(self):
     print(f"Current balance: {self.balance}")

                    ###Logic Section###

print("Welcome to Digital Bank")
name = input("Please enter your name: ")

my_account = BankAccount(name,500)
while True:
    print("\nPlease choose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        my_account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        my_account.withdraw(amount)
    elif choice == '3':
        my_account.show_balance()
    elif choice == '4':
        print("Thanks for using Digital Bank Take love from Mahatab :)!")
        break
    else:
        print("Invalid choice, please try again.")
