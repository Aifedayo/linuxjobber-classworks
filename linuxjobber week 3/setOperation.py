#Set Operations

set1 = {1,2,3,4,5}
set2 = {0,9,8,7,6,5,4,3,2,1}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference = (set1) - (set2)

print(difference)

sym_diff = set1 ^ set2
print(sym_diff)