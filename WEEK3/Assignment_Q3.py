#calculator class using exception handling


class Calculator:
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
		return self.a + self.b
	def sub(self):
		return self.a - self.b
	def mul(self):
		return self.a * self.b
	def div(self):
		return self.a / self.b

print("""===== CALCULATOR =====""")
try:
	a = int(input("enter the value of a : "))
	b = int(input("enter the value of b : "))

	cal = Calculator(a,b)

	while True :
		print (""" choose the operations :
	1 - addition
	2 - subtraction
	3 - multiplication
	4 - division""")
		opt = int(input(">>> "))
		if opt == 1 :
			print ( cal.add())
		elif opt == 2:
			print (cal.sub())
		elif opt == 3:
			print (cal.mul())
		elif opt == 4:
			print (cal.div())
		elif opt ==5:
			break
		else:
			print ("Invalid input ")


except ValueError:
	print ("invalid value check it once")
except ZeroDivisonError:
	print ("while performing divison denominator not equals to 0")


