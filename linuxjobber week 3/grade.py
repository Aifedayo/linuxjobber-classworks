#Nested if and multi-way if elif else

score = int(input('Enter your score here: '))
if score >= 80:
	print('Grade is A')
elif score >= 70:
	print('Grade is B')
elif score >= 60:
	print('Grade is C')
elif score >= 50:
	print('Grade is D')
elif score >= 40:
	print('Grade is E')
else:
	print('Grade is F')