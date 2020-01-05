#Summing elements by column

matrix = [[6,2,3], [4,5,6], [7,8,9]]

print([sum(x) for x in zip(*matrix)])