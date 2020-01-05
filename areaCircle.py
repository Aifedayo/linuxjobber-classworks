# Calculating the area of a circle

#Importing pi from the math module
from math import pi


r = int(input("Enter the radius of the circle: "))
area = pi*(r**2)

#reducing to 2 significant figures

print("The area of the circle is: ", format(area, '.2f'))