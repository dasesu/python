"""
054
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.
"""

import random
coin = random.choice(["h","t"])
user_choice = input("select a choice, (h)ead or (t)ail?")
if user_choice == 'h' or user_choice == 't':
   if coin == user_choice:
      print("You win")
   else:
      print("Bad luck,")
   if coin == 'h':
      print("it was heads")
   else:
      print("it was tail")
else:
   print("wrong selection, try again")