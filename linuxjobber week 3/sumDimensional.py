#Summing all Elements

total = 0
list7 = [[6,6,7,8,9], [0,9,8,6,7], [0,8,0]]
for i in list7:
	for num in i:
		total +=num
	
print ("The sum of the multidimensional list is: ", total)