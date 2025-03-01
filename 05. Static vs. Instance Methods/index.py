# ==============================================================================
# Static Methods 
# ==============================================================================

#  Belong to the class itself, but dont access instance(self) or class(cls) attributes
# Defined using @staticmethod decorator

# ==============================================================================
# Instance Methods
# ==============================================================================

# Belong to the instance of the class
# Take self as the first parameter, for representing the instance
# Can access and modify class and instance


class BankAcc:
    
    MIN_BALANCE = 1000
    
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    # Instance Method
    def deposit(self, amount):
        if self._isValidAmount(amount):
            self._balance += amount
            print(f'{self.owner} deposited {amount}. New balance: {self._balance}')
            self.__logTransaction('deposit', amount)
        else:
            print("Amount must be positive")
            return 'Invalid amount'
    
    # Protected Method
    def _isValidAmount(self, amount):
        return amount > 0   
    
    # Private Method
    def __logTransaction(self, transactionType, amount):
        print(f'Logging {transactionType} of ${amount}. New balance: {self._balance}')
      
    # Static Method
    @staticmethod
    def isValidInterestRate(rate):
        return 0 <= rate <= 5
    
account1 = BankAcc('Hasindu', 10000)
account1.deposit(1000)
    
print(BankAcc.isValidInterestRate(3))
print(account1.isValidInterestRate(10)) # This will not work as it is a static method

# account1._isValidAmount(100) # This will not work because it is a protected method
# account1.__logTransaction('deposit', 100) # This will not work because it is a private method