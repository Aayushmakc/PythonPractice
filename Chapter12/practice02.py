# Create Account class with 2 attributes-balance &Account no.Create methods for debit,credit&printing the balance
class Account:
  def __init__(self,bal,acc) :
    self.balance=bal
    self.account=acc

    #debit method
  def debit(self,amount):
      self.balance-=amount
      print("Rs." ,amount, "has been debited from your account")
      print("total balance",self .get_balance())

  def credit(self,amount):
      self.balance+=amount
      print("Rs." ,amount, "has been credited from your account")

  def get_balance(self):
      return self.balance





acc1=Account(100000,1234555)
acc1.debit(1000)
acc1.credit(2000)
acc1.credit(40000)

    