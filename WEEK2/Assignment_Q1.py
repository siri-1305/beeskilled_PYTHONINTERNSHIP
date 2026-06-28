#creat contact book using dictionary
from termcolor import colored
contact = dict()

def add():
	key = input("enter the contact name : ")
	val = input("enter the contect no : ")
	if key in contact.keys():
		print (colored("contact already existed!","red"))
	else:
		contact[key]=val
		print (colored("contact added ","green"))
def search():
	key = input("enter the contact name to search :")
	if key in contact.keys():
		print (colored(f"{key} : {contact[key]}","green"))
	else:
		print (colored("Contact not found !","red"))
def update():
	key = input("enter the contact name to update : ")
	if key in contact.keys():
		val=input("enter the new contact no : ")
		contact[key]=val
		print (colored("Updated !","green"))
	else:
		print (colored("contact not found ","red"))
def delete():
	key = input("enter the contact name to delete : ")
	if key in contact.keys():
		del contact[key]
		print (colored("contact deleted!","green"))
	else:
		print (colored("contact not found","red"))

while True :
	print ( """ select the following options :
			- 1 to  Add Contact
			- 2 to Search Contact
			- 3 to Update Contact
			- 4 to Delete Contact
			- 5 to Exit Contact Book
		""")
	opt = int(input( " >>> "))
	if (opt == 1 ):
		add()
	elif (opt == 2 ):
		search()
	elif ( opt == 3 ):
		update()
	elif (opt == 4 ):
		delete()
	else:
		exit()

