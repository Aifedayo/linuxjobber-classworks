from math import acos

a = int(input("Input a value for a: "))
b = int(input("input a value for b: "))
c = int(input("input a value for c: "))

# seperating into parts to make the formula readable

angle_1 = acos
angle_2 = (a*a)+(b*b)-(c*c)
angle_3 = (2*b*c)

A = angle_1((angle_2/angle_3))

print (A)