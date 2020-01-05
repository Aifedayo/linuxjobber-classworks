# Calculating the Area of a pentagon

from math import tan, pi

s = int(input('Enter the length of the side of the pentagon: '))

a = (pi/5)

Area  = 5 * s * 24 * (tan(a))

print("The area of the pentagon is: ", format(Area, '.2f'))