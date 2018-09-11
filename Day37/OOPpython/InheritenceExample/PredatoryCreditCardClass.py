## the credit card logic was created on day 36

## We'll be adding to that class to create a specialized class from that super class. TODO: Find out if you can just use 'dll' like compiled languages where you can 
## have the logic in a sort of encapsulated manner

## PredatoryCreditCard will change the  charge method (override the superclass - is this a base class ?)
## and change the ctor to contain an additional param

from creditCardClass import CreditCard # I have to import it I think ?

class PredatoryCreditCard(CreditCard): # so you'd inherit like this ? Does py support multiple inheritance

    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Createa a new Predatory Credit card instance
        
        The inital balance is zero

        customer the name of the customer (e.g., John Bowman )
        bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """

        super().__init__(customer, bank, acnt, limit) # This would be a call to the supers ctor (super() is a method that acts as the super classes instance)
        self._apr = apr # the super ctor handles everything but this, this is how we would extend a class
    
    # I'm assuming that if the method name is the same in the super class it is overwritten ?
    def charge(self, price):
        """
        Charge given to the card, assuming sufficient credit limit

        Return True if charge was processed
        Return False and assess $5 fee if charge is denied # Note, this differs in the base class (super class ?)
        """
        
        success = super().charge(price)    # we call the inherited method 
        if not success:
            self._balance += 5             # the penalty is added to the balance ? Not sure if I understand ?
        return success                     # caller expects return value

    # adding a new method (Just like adding a normal method)
    def process_month(self):
        """
        Assess monthly interest on outstanding balance
        """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor # read page 86 for the math behind this