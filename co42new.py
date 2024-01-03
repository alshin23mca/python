class bank:
	def __init__(self,acc_number,name,balance):
		self.acc_number=acc_number
		self.name=name
		self.balance=balance
	def deposit(self,amount):
		if amount>0:
			self.balance=self.balance+amount
			print(" Money deposited !!")
			print(" Current balance :",self.balance)
	def withdraw(self,amount):
		if amount>0:
			if amount>self.balance:
				print("Cannot Withdraw!!")
			else:
				self.balance=self.balance-amount
				print("Money Withdrawn!! ")
				print("Current Balance :",self.balance)
		else:
			print("Enter proper amount!")

acc_number=int(input("Enter account number :"))
name=input("Enter account Name :")
balance=int(input("Enter Balance:"))
customer=bank(acc_number,name,balance)
flag=True
while(flag==True):
		print("Enter the Operation 1.Deposit 2. Withdraw 3. Exit ")
		op=int(input("Ente the operation : "))
		if op==1:
			amount=int(input("Enter the amount to be deposited :"))
			customer.deposit(amount)
		elif op==2:
			amount=int(input("Enter the amount to be Withdraw :"))
			customer.withdraw(amount)
		elif op==3:
			flag=False
		else:
			print("Enter correct operation!! ")
