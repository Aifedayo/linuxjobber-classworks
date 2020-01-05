#Program to calculate the area and volume of a cylinder

from math import pi

r = int(input("Insert the value for the radius here in m: "))

h = int(input("insert the value for the height here in m: "))
#Area
A = (2*pi*r**2) + (2*pi*r*h)

#Volume
V = (pi*r**2*h)

print("The area of the cylinder is: ", format(A,'.2f'), 'm2')

print("The volume of the cylinder is: ", format(V, '.2f'), 'm3')