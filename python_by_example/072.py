''' Create a list of six school subjects. Ask the user which of these
subjects they don’t like. Delete the subject they have chosen from the
list before you display the list again. '''

subjects = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"]
for i in range(len(subjects)):
   print(subjects[i], end=" ")
print(" ")
unlike = input("introduzca un tema que no te guste: ")
indice = subjects.index(unlike)
print(f"se eliminara {subjects[indice]}")
del subjects[indice]
for i in subjects:
   print(i),
