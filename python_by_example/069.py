'''Create a tuple containing the names of five countries and display the whole tuple. Ask
the user to enter one of the countries that have been shown to them and then display
the index number (i.e. position in the list) of that item in the tuple.'''

countries_tuple = ("Irlanda", "Venezuela", "Portugal", "Italy", "Spain")
print(countries_tuple," ")
country = input("Introduce alguno de ellos: ")
print( country, "tiene el indice" , countries_tuple.index( country ))

'''Add to program 069 to ask the
user to enter a number and
display the country in that
position.'''

indice = int(input("Introduce un numero "))
print( f"La posicion {indice} contiene al pais ", countries_tuple[indice] )