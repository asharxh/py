class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: $ {self.balance}")
        else:
            print(" Deposite amount must be positive. ")
            
    def withdraw (self, amount):
        if amount > self.balance:
            print(" Insufficient funds. ")
        elif amount <= 0:
            print("Deposite amount must be positive. ")
        else:
            self.balance -= amount
            print(f" Withdrew ${amount}. New balance: ${self.balance}")
            
    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        
def main():
    print(" Welcome to the Bank Account Simlutor: ")
    name = input("Enter your name: ")
    account = BankAccount(name)
    
    while True:
        print("\n --Menu--")
        print("1: Deposite")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposite(amount)
        elif choice == "2":
            amount =float(input("Enter withdraw amount"))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print(" Thank you for using the Bank Account Simulator ")
            break
        else:
            print(" Invalid Choice, Try Again")
                  
main()
