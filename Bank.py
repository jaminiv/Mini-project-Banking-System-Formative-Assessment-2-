class BankAccount:
    def __init__(self, name, username, password, balance=0):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount} successfully. Current balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def __str__(self):
        return f"Account Holder: {self.name}, Balance: {self.balance}"


def login(accounts):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for account in accounts:
        if account.username == username and account.password == password:
            print(f"Welcome, {account.name}!")
            return account
    print("Invalid username or password.")
    return None


def main():
    accounts = [
        BankAccount("Jamini D V", "Jamini", "password123"),
        BankAccount("Vinson ET", "Vinson", "abc123")
    ]

    account = login(accounts)
    if not account:
        return

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
