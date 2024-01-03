class Bank:
	def __init__(self,accno,name,atype,balance):
		self.accno=accno
		self.name=name
		self.type=atype
		self.balance=balance
	def deposit(self,amount):
		if amount>0:
			self.balance+=self.balance+amount
			print("Money credited!!!")
		else:
			print("Invalid")
	
	
	def withdraw(self, amount):
		if 0 < amount <= self.amount:
			self.balance-=self.balance+amount
			return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
		elif amount > self.balance:

			return "Invalid"
	def get_balance(self):
		return f"Current balance: ${self.balance}"
		
		
account1=Bank("1001","John Doe","Savings",1000)
print(account1.get_balance())		
deposit_result = account1.deposit(500)
print(deposit_result)
withdrawal_result=account1.withdraw(200)
print(withdrawal_result)
print(account1.get_balance())
		


