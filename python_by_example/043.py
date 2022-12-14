"""
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message I don’t understand
"""

direction = input("select wich direction: ")
if direction == "up":
   top_number = int(input("introduce a top number "))
   for i in range(0,top_number+1):
      print(i)
elif direction == "down":
   below_20 = int(input("introduce a top number lower than 20: "))
   for i in range(20,below_20-1,-1):
      print(i)
else:
   print("i don\'t understand")
