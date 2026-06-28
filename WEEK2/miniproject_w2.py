from termcolor import colored
import csv
print ("""===============================
   student management system
===============================""")
FILE_NAME = input("enter the path of csv file : ")

def add():
    name = input("Enter Student Name : ")
    roll = input("Enter Roll Number : ")
    marks = input("Enter Marks : ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, roll, marks])

    print(colored("Student Added Successfully!","green"))


def display():
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)

        print("\n------ Student List ------")

        for row in reader:
            print("{:<15}{:<10}{:<10}".format(row[0], row[1], row[2]))

        print()


def search():
    roll = input("Enter Roll Number to Search : ")

    found = False

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)

        next(reader)  # Skip header

        for row in reader:
            if row[1] == roll:
                print(colored("\nStudent Found","green"))
                print("Name :", row[0])
                print("Roll :", row[1])
                print("Marks:", row[2])
                found = True
                break

    if not found:
        print(colored("Student Not Found!","red"))


def delete():
    roll = input("Enter Roll Number to Delete : ")

    rows = []

    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)

        header = next(reader)
        rows.append(header)

        found = False

        for row in reader:
            if row[1] != roll:
                rows.append(row)
            else:
                found = True

    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if found:
        print(colored("Student Deleted Successfully!","green"))
    else:
        print(colored("Student Not Found!","red"))


while True :
	print ("""\nselect the following options :
1 - Add students
2 - Search students
3 - Delete students
4 - Display students
5 - Exit""")
	opt = int(input(">>> "))
	if ( opt == 1 ):
		add()
	elif ( opt == 2 ):
		search()
	elif ( opt == 3 ):
		delete()
	elif ( opt == 4 ):
		display()
	elif ( opt == 5 ):
		break
	else:
		print (colored("Invalid choice","red"))
