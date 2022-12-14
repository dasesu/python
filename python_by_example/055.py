"""
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”.
"""

import random

num = random.randint(1,5)
choice = int(input("Select a number between 1 and 5: "))
if choice == num:
   print("Well done")
else:
   if choice > num:
      print("Too high, try again")
   else:
      print("Too low, try again")
choice = int(input("Select a number between 1 and 5: "))
if choice == num:
   print("Correct")
else:
   print("You lose")
   # print(f"The number was {num}")
   print("The number was",num)