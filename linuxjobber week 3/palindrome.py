#Palindrome Number

num = int(input('Enter a three digit number: '))
reverse = int(str(num)[::-1])
if num == reverse:
	print('It is a palindrome')

else:
	print('It is not a palindrome')