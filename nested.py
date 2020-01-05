'''Nested loop using while and for 
'''

#predefining i
i = 0
while i !=14:
	for i in range(int(input('enter a lower limit:  '
)), int(input('enter the upper limit: ')) + 1):
		if i%2 == 0:
			print(i, 'it is even number')
		else:
			print(i, 'it is not an even number, it is an odd number')
	if i == 14:
		break