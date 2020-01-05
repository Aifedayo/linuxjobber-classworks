#Find future Dates
print("Follow the below instructions carefully")
print('Sunday = 0 \n Monday = 1 \n Tuesday = 2 \n Wednesday = 3 \n Thursday = 4 \n Friday = 5 \n Saturday = 6' )

todayDate = int(input("Enter today's date: "))
future_date = int(input("Enter the number of days: "))
futureDate = todayDate + future_date

while todayDate <= 6:
	
	if  futureDate % 7 == 0:
		print('Sunday')
		break
	elif  futureDate % 7 == 1:
		print('Monday')
		break
	elif  futureDate % 7 == 2:
		print('Tuesday')
		break
	elif futureDate % 7 == 3:
		print('Wednesday')
		break
	elif futureDate % 7 == 4:
		print('Thursday')
		break
	elif futureDate % 7 == 5:
		print('Friday') 
		break
	elif futureDate % 7 == 6:
		print('Saturday')
		break
else:
	print('Outside range of days within a week')