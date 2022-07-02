"""
Display the following message:

1) square
2) triangle

If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.
"""
menuselection = 0
print(" 1) square")
print(" 2) triangle")
print()
menuselection = int(input("enter a number: "))
if menuselection == 1:
   side = int(input("enter a side: "))
   area = side*side
   print("the area is ", area)
elif menuselection == 2:
    base = int(input("enter a base: "))
    height = int(input("enter a height: "))
    area = base*height
    print("the area is ", area)
else:
    print("wrong option")

