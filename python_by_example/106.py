'''
Create a new file called “Names.txt”. Add five names to the
document, which are stored on separate lines. Once you have
run the program, look in the location where your program is
stored and check that the file has been created properly.'''

file = open("names.txt","w")
file.write("Sebastian\n")
file.write("Maria\n")
file.write("Lorena\n")
file.write("Carlos\n")
file.write("Jesus\n")