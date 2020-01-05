def fib(n):
	fibs = [0,1]
	for i in range(1,n +1):
		fibs.append(fibs[-1] + fibs[-2])
		
	return fibs
result = fib(n = int(input('Enter a number: ')))
print(result)