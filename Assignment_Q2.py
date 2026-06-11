#STUDENT GRADE CALCULATOR

n = int ( input ("enter no of subjects : "))

marks  = []

for i in range(0,n):
	a = int (input(f"enter the marks of sub{i} : "))
	marks.append(a)
s = sum(marks)
a = s/n
print ( "The average of marks : ",a)

if ( a > 90 ):
	print ("you got GRADE A!")

elif ( 90>a>80):
	print ("you got GRADE B!")

elif ( 80>a>70):
	print ("you got GRADE C")

elif (70>a>60):
	print("you got GRADE D")

elif (60>a>50 ):
	print ("you got GRADE E ")

else:
	print("sorry u failed try again!")
