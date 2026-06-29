#BILLING SYSTEM 

print ("========== BILLING SYSTEM ==========")

class Product:
	def __init__(self,name,price,quantity):
		self.name = name
		self.price = price
		self.quantity = quantity
	def total1(self):
		return self.price * self.quantity
class Bill:
	def __init__(self,total,tax):
		self.total = total
		self.tax = tax
	def bill(self):
		t = self.total*(self.tax/100)
		bill = self.total + t
		print ("The total amount is : ",self.total)
		print ("The total tax is : ",t)
		print (" The total bill is : ",bill)



p = Product("rice",10,50)

total = p.total1()

b= Bill(total,18)

b.bill()
