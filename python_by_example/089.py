'''Create an array which will store a list of integers.
Generate five random numbers and store them in
the array. Display the array (showing each item on
a separate line).'''


from array import *
import random

myArray = array ('i', [])
for i in range(0,5):
   num = random.randint(1,100)
   myArray.append(num)

for i in myArray:
   print(i)
