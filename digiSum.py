#Calculating the sum of digits between 1 to 1000

#getting the integers between 1 to 1000
for i in range(1, 1000):
	
#declaring variables to hold individual digits
	p =  i//10
	x =  i%10
	y = p//10
	z = p %10
# Summing the digits
	A =  x + y + z
	print(i, 'is equal to', A)