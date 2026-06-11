#TEMPERATURE CONVERTOR


def cel_to_far(num):
	a = (num*9/5)+32
	return a

def far_to_cel(num):
	b = (num-32)*5/9
	return b


def main():
	option = input('''select the following options :
	enter 1 for celsius to fahrenheit conversion
	enter 2 for fahrenheit to celsius conversion\n
>>> ''')
	result = None
	num = int(input(" enter the value for conversion : "))  
	if option == "1" :
		result = cel_to_far(num)
	else:
		result = far_to_cel(num)

	print ( " The final result is : " ,result)

main()
