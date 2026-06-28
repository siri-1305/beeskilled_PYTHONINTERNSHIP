#create a word counter

path = input("enter the text file name along with path   : ")

f = open(path,"r")

text = f.read()

words = text.split()

lines = text.splitlines()

characters = len(text)

print (f""" no of words      : {len(words)}
 no of lines      : {len(lines)}
 no of characters : {characters}""")


