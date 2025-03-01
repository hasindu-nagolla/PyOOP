# ==============================================================================
# Static Methods 
# ==============================================================================

#  Belong to the class itself, but dont access instance(self) or class(cls) attributes
# Defined using @staticmethod decorator


class BankAcc:
    
    minimumBalance = 1000
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'{self.owner} deposited {amount}. New balance: {self._balance}')
            return self._balance
        else:
            print("Amount must be positive")
            return 'Invalid amount'
        
    @staticmethod
    def isValidInterestRate(rate):
        return 0 <= rate <= 5
    
account1 = BankAcc('Hasindu', 10000)
account1.deposit(1000)
    
print(BankAcc.isValidInterestRate(3))
print(account1.isValidInterestRate(10)) # This will not work as it is a static method