class Bankaccount:
  def __init__(self,account_number,account_h_name,account_type,balance=0):
   self.account_number=account_number
   self.account_h_name=account_h_name
   self.account_type=account_type
   self.balance=balance
 
  def deposite(self,amount):
   if amount>0:
     self.balance += amount
     print("success deposite of",amount)
     print("new balance:",self.balance)
   else:
     print("invalid")
  def withdraw(self,amount):
     if 0<amount<=self.balance:
         self.balance-=amount
         print("withdraw succeccfull and balance=",self.balance)
     elif amount>self.balance:
         print("withdrw unsuccess full")
     else:
         print("invalid amount please enter a positive value")
  def get(self):
         print("current balance:",self.balance)

account1 = Bankaccount("1001","Alshin","Savings","1000")

account1.get()
deposite_result = account1.deposite(500)
account1.get()
withdrawal_result = account1.withdraw(200)
