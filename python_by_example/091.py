'''Create an array which contains
five numbers (two of which
should be repeated). Display
the whole array to the user. Ask
the user to enter one of the
numbers from the array and
then display a message saying
how many times that number
appears in the list.'''

from  array import *

myArray = array('i', [2,4,5,6,7,4,8])

for i in myArray:
   print(i, end = " ")

print()
numero = int(input("Introduzca algun numero contenido en el array: "))
if myArray.count(numero) != 1:
   print("El numero", numero, "aparece", myArray.count(numero), "veces")
else:
   print("El numero", numero, "aparece una vez")