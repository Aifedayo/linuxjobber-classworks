#The row with the largest sum
import math
list1 = []
list8 = [[0,9,8,7], [0,0,9,8],[4,5,6,7]]
for i in list8:
	list1.append(sum(i))
maxRow = list(list1)
print(maxRow)

indexOfMaxRow = maxRow.index(max(maxRow))
print(indexOfMaxRow)

