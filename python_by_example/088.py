'''Ask the user for a list of five
integers. Store them in an array.
Sort the list and display it in
reverse order'''

from array import *

integers = array('i',[])
for val in range(0,5):
   currentValue = int(input("Introduce un valor: "))
   integers.append(currentValue)

for i in integers:
   print(i, end = " ")

print()