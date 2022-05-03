""" 023
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts
counting from 0 and not 1) """

from traceback import print_tb


phrase = input("insert some frase")
length =  len(phrase)
print(f'this has {length} letters in it')
start = int(input("were start?: "))
end = int(input("were end?: "))
part = phrase[start:end]
print( part )