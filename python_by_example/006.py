#006
#Ask how many slices
#of pizza the user
#started with and ask
#how many slices
#they have eaten.
#Work out how many
#slices they have left
#and display the
#answer in a user-
#friendly format.

slices = int(input("with how many slaces do you start: "))
eated = int(input("how many slices do you ate?: "))

result = slices - eated
print("there are", result, "slices remaining")

