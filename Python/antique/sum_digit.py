num = 78

def sum_digit(number):
    return sum([int(i) for i in str(number)])

while num > 10:
	num = sum_digit(num)

print(num)