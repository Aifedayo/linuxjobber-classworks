#Accepting input from users

principal = int(input("Enter the value for Principal: "))
rate = int(input("Enter the value for Rate: "))
time = int(input("Enter the value for Time: "))

simple_interest = principal * rate * time
print(" The value for the calculated simple interest is: ",simple_interest)