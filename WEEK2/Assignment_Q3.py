#create JSON file reader and print formatted output
import json
path = input("enter the path of json file : ")
f = open(path,'r')

data = json.load(f)

for i,j in data.items():
	print ( i,":",j )

