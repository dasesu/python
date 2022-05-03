#015
#Ask the user to enter their favourite colour. If they enter “red”, “RED” or
#“Red” display the message “I like red too”, otherwise display the message
#“I don’t like [colour], I prefer red”.

color = input("what is your favorite color?")

if color == "RED" or color == "Red":
   print("i like red too")
else:
   print("i dont like ", color, "i prefer red")