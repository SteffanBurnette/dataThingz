class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self. balance += amount
        print(f"{amount} is deposited. New balance is {self.balance}")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"You do not have enough in your account to take out {amount}")
            print(f"Your current balance is {self.balance}")    
        else:
            self.balance -= amount
            print(f"{amount} was sucessfully withdrawn. Remaining balance is {self.balance}")

    def get_balance(self):
        return self.balance

new_user = BankAccount("jeff", 1000)
print(f"Hello {new_user.owner}, you current balance is {new_user.balance}")
new_user.deposit(int(input("How much would you like to deposit: ")))
new_user.withdraw(int(input("How much would you like to take out: ")))

print(f"Your final balance is {new_user.balance}")