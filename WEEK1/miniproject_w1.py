#SIMPLE ATM SIMULATOR
def check_balance(balance):
	print ( "CURRENT BALANCE : ",balance)
	
def deposit(balance):
	a = int ( input (" enter the amount you want to deposit : "))
	balance = balance + a
	return balance
	
def withdraw(balance):
	a = int ( input (" enter the amount you want to withdraw : "))
	balance = balance - a
	return balance



def main():
	print ( '''===================================================================================
                                 WELCOME TO ATM SIMULATOR
===================================================================================''')
	pin = "1234"
	balance = 1000
	p = input ( " Enter the PIN CODE to continue : ")
	if p==pin:
		while(True):
			print ('''SELECT THE OPTIONS BELOW ACCORDING TO YOUR REQUIREMENTS
			[1] for CHECKING BALANCE
			[2] for DEPOSIT
			[3] for WITHDRAW
			[4] for EXIT''')
			opt = int (input(">>>"))
			if ( opt==1 ):
				check_balance(balance)
			elif ( opt==2 ):
				balance=deposit(balance)
			
			elif ( opt==3 ):
				balance=withdraw(balance)
			else:
				print ("THANK YOU ! VISIT AGAIN ..")
				exit()
	else:
		print ( "WRONG PIN ")
main()
