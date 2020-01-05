#A two way if-else statement

pay = int(input('Enter your pay here: '))

if pay > 90:
	pay_rise = pay * 0.03
	new_pay = pay_rise + pay
	print('Your new pay is: ', new_pay)
	
else:
	pay_rise = pay * 0.01
	new_pay = pay_rise + pay
	print(' Your new pay is: ', new_pay)
