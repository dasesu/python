""" 022
Ask the user to enter their first name and surname in lower
case. Change the case to title case and join them together.
Display the finished result """

name = input("Enter your first name: ")
surname = input("Enter your surname: ")
all = name + " " + surname
print(all.title())

