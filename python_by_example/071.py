'''Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it.'''

sports = ["futbol", "baloncesto"]
for i in sports:
   print( i )

favorite = input("Cual es tu deporte favorito?: ")
sports.append(favorite)
for i in sorted(sports):
   print( i )