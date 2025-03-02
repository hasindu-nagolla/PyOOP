# Encapsulation is the practice of restricting direct access to some of an object's components. Its mean hide internal data from the outside.

class NotSecureBandAccount:
    def __init__ (self, balance):
        self. balance = balance

notSecureBankAccount = NotSecureBandAccount(0.0)
notSecureBankAccount.balance = -10
print(notSecureBankAccount.balance)


# ==============================================================================
# Create a SecureBandAccount class using encapsulation in OOP
# ==============================================================================

class SecureBandAccount:
      
    def __init__ (self):
        self. _balance = 0.0
    
    @property
    def balance(self):
        return self._balance
    
    
    def deposit(self, amount): # Deposit method
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self._balance += amount
        print(f'Deposited {amount}. New balance: {self._balance}')
        
        
    def withdraw(self, amount): # Withdraw method
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        self._balance -= amount
        print(f'Withdrew {amount}. New balance: {self._balance}')


secureBankAccount = SecureBandAccount()
print(secureBankAccount.balance)

# secureBankAccount.balance = -10 # This will not work because balance is a read-only property

secureBankAccount.deposit(1999)
print(secureBankAccount.balance)

secureBankAccount.withdraw(992)
print(secureBankAccount.balance)