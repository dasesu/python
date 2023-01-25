'''
Enter a list of ten colours. Ask the user for a start number 
between 0 and 4 and an end number between 5 and 9. Display the
 list for those colours between the start and end numbers the user input.
'''

colours = ["red", "blue", "green", "black", "white", "pink", "grey", "purple", "yellow", "brown"]
print(colours)
start = int(input("start number between 0 and 4: "))
while (start < 0) or (start > 4):
   start = int(input("start number between 0 and 4: "))

end = int(input("end number between 5 and 9: "))
while (end < 5) or (end > 9):
   end = int(input("end number between 5 and 9: "))

print(colours[start:end])