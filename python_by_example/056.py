"""
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked.
"""

import random

num = random.randint(1,10)

choice = 0
choice = int(input("Select a number between 1 and 10: "))
while choice != num:
   choice = int(input("Try again: "))
print(f"{num}, that's Correct!")