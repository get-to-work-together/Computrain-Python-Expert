class BankAccount:
    """Demo class for OO
    """

    def __init__(self, name, iban, balance = 0.0):
        """_summary_

        Parameters
        ----------
        name : _type_
            _description_
        iban : _type_
            _description_
        balance : float, optional
            _description_, by default 0.0
        """        

        self._name = name
        self._iban = iban
        self._balance = round(balance)


    def __str__(self):
        return f'Account {self._iban} - {self._name}: {self._balance:.2f}.'

    def __repr__(self):
        return f'BankAccount("{self._name}", "{self._iban}", {self._balance})'

    def __del__(self):
        print(f'Your account {self._iban} has been terminated!')

    def __eq__(self, other):
        return self._balance == other._balance
    def __ne__(self, other):
        return self._balance != other._balance
    def __gt__(self, other):
        return self._balance > other._balance
    def __ge__(self, other):
        return self._balance >= other._balance
    def __lt__(self, other):
        return self._balance < other._balance
    def __le__(self, other):
        return self._balance <= other._balance
    
    @property
    def balance(self):
        """Getter for balance attribute"""
        return round(self._balance, 2)
    
    @balance.setter
    def balance(self, value):
        self._balance = round(value, 2)

    def deposit(self, amount):
        self._balance = round(self. _balance + amount, 2)

    def withdraw(self, amount):
        self._balance = round(self. _balance - amount, 2)

    def info(self):
        return f'Account {self._iban} is owned by {self._name} and has a balance of {self._balance:.2f}.'
    

# --------------------------------------------------------------------------------------------

acc1 = BankAccount('Peter', 'NL99ABCD09876543522')
acc2 = BankAccount('Jan', 'NL99ABCD09876543523')

print(acc1.info())

acc1.deposit(100)
acc1.deposit(200)
acc2.deposit(34)

print(acc1.info())

print(acc1.__dict__)

print(acc1)
print(str(acc1))
print(repr(acc1))

if acc1.balance > acc2.balance:
    print('Acc1 is larger')
else:
    print('Acc2 is larger')

acc1.balance = 100000.12345678

print(acc1.balance)
print(acc2.balance)

