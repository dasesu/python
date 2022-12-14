#012
#Ask for two numbers. If
#the first one is larger
#than the second, display
#the second number first
#and then the first
#number, otherwise show
#the first number first and
#then the second.

number1 = int(input("enter a number: "))
number2 = int(input("enter another number: "))

if number1 < number2:
   print(number2)
   print(number1)
else:
   print(number1)
   print(number2)
