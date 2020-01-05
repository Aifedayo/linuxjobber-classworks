# Calculating the gratuity and tips

sub_total = int(input('enter your sub total value here: '))

g = int(input("insert your gratuity value in percentage here: "))

gratuity_rate = g/100

total = sub_total + gratuity_rate

print(gratuity_rate)
print(total)