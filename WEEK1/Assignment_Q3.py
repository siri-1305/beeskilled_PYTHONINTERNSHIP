#EVEN/ODD & PRIME NUMBER CHECKER

def even_odd(num):
	if (num%2==0):
		print( "The number is even !" )
	else:
		print( "The number is odd !")


def prime_nor(num):
	c=0
	for i in range(1,num+1):
		if(num%i==0):
			c=c+1
	if(c==2):
		print ("The number is prime !")
	else:
		print ("The number is not a prime !")


def main():
	num = int (input (" Enter the number you want to check for even/odd & prime checker : "))
	even_odd(num)
	prime_nor(num)

main()
