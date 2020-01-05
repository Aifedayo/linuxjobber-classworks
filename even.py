# A for loop to print even and odd number 

#Specifying the upper limit and lower limit

for i in range(int(input('enter a number: '
)), int(input('enter the upper limit: ')) + 1):
	if i%2 == 0:
		print(i, 'it is even number')
	else:
		print(i, 'it is not an even number, it is an odd number')
		
# Specifying the end of the loop 
print('Done and dusted')
		