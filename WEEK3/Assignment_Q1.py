#Bank Account class
from termcolor import colored
class Account:
	def __init__(self,name,balance):
		self.balance = balance
		self.name = name
	def deposit(self,amount):
		self.balance = self.balance + amount
		print (colored( " amount is deposited! ","green"))
	def withdraw(self,amount):
		self.balance = self.balance - amount
		print (colored(" amount is withdrawed! ","green"))
	def display(self):
		print (colored (f"The balance amount is {self.balance}","green"))


obj = Account("sameera",5000)
obj.deposit(1000)
obj.display()
obj.withdraw(2000)
obj.display()
