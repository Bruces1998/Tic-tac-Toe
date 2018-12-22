"""
Bank Account project using Object Oriented Programming in Python
"""

class Account():
    
    def __init__(self,name,account_no,balance=0):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        
    def withdraw(self,amount):
        if(amount < self.balance):
            self.balance=self.balance-amount
            print('Transaction Successful!')
        else:
            print('Insufficient Balance')
            
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Deposit Successful')
        
    def __str__(self):
        return('NAME:{} \nACCOUNT NO{}\nBALANCE:{}'.format(self.name,self.account_no,self.balance))
