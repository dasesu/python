'''
Open the Names.txt file. Ask the user to input a
new name. Add this to the end of the file and
display the entire file. '''

file = open("names.txt","a")
name = input("Whats your name bob?\n")
file.write("\n"+name)
file.close()

file = open("names.txt","r")
print(file.read())