# Python Program to display all the prime numbers within an interval

lower = 1
upper = 10


print("Prime Numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
	# All Prime Numbers are greater than 1
	print("number ",num)
	if num > 1:
		for i in range(2, num):
			if (num % i) == 0:
				break
		else:
			print(num)
