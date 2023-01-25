'''Ask the user to enter four of their favourite 
foods and store them in a dictionary so that they
are indexed with numbers starting from 
1. Display the dictionary in full, showing 
the index number and the item. Ask them which
they want to get rid of and remove it from the list.
Sort the remaining data and display the dictionary.'''

food_dictionary = {}

i=1;
while i < 5:
   food_dictionary[i] = input("enter your favorite food: ")   
   i=i+1
print( food_dictionary )
dislike = int(input("indica el indice de cual te gustaria remover?: "))
del food_dictionary[dislike]
print( food_dictionary.values() )
