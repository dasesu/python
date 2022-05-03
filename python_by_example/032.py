"""
Ask for the radius and the depth of a cylinder
and work out the total volume (circle
area*depth) rounded to three decimal
places.
"""
import math

radius = float(input("enter a radius of a cylinder: "))
depth = float(input("enter a depth of a cylinder: ") )

area = (math.pi*(radius**2))
volume = round((depth*area),2)
print(f"El volumen es: {volume}")
