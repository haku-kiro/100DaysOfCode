class CreditCard:
    """
    A consumer credit card
    """
    
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance
        
        The initial balance is zero

        customer  The name of the customer
        bank      The name of the bank
        acnt      The account identifier
        limit     Credit limit
        """
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """
        Return the name of the customer
        """
        return self._customer

    def get_bank(self):
        """
        Return the name of the bank
        """
        return self._bank

    def get_account(self):
        """
        Return the account number
        """
        return self._acnt

    def get_limit(self):
        """
        Return the accounts limits
        """
        return self._limit

    def get_balance(self):
        """
        Return the accounts balance
        """
        return self._balance

    def charge(self, price):
        """
        Charge the given price to the card, assuming sufficient credit limit

        Return True if the charge was successful, False if not
        """
        if price + self._balance > self._limit:
            # that is, the charge exceeds the limit
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, amount):
        """
        Processe a customer payment that reduces the account balance
        """
        self._balance -= amount