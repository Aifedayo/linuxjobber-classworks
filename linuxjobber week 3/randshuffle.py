import random

list9 = [[6,6,7,8,9], [0,9,8,6,7], [0,8,0]]
for row in range(len(list9)):
	for column in range(len(list9[row])):
		i = random.randint(0,len(list9)-1)
		j = random.randint(0, len(list9[row])-1)
		
		list9[row][column], list9[i][j] = list9[i][j], list9[row][column]
		print(list9)