#Factorial

n = int(input("Enter a number here: "))
def recFactorial(n):
	if n == 0:
		return 1	
	return n* recFactorial(n-1)
			
result = recFactorial(n)
print(result)
