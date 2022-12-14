# 017
# Ask the user’s age. If they
# are 18 or over, display the
# message “You can vote”, if
# they are aged 17, display the
# message “You can learn to
# drive”, if they are 16, display
# the message “You can buy a
# lottery ticket”, if they are
# under 16, display the
# message “You can go Trick-
# or-Treating”

age = int(input("what is your age?"))
if age >= 18:
   print("you can vote")
elif age == 17:
   print("you can learn drive")
elif age == 16:
   print("you can buy a lotery ticket")
else:
   print("you can go trick-or-treating")
   