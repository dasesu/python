"""
Ask the user to enter two numbers.
Use whole number division to divide
the first number by the second and
also work out the remainder and
display the answer in a user-friendly
way (e.g. if they enter 7 and 2 display
“7 divided by 2 is 3 with 1
remaining”).
"""
import math

one = int(input("enter a number: "))
two = int(input("again, enter a number: ") )
remaining = one % two

print(f"{one} dived by {two} is {one//two} with remaining {remaining}")
