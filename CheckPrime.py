# Program to check if a number is prime or not

num = int(input("Please Enter a Number between 1 to 50: "));

# Prime Numbers are greater than 1

if num > 1:
	#Check for factors
	for i in range(2,num):
		if (num % i) == 0:
			print(num, " is not a prime number");
			print(i, " times ", num//i, " is ", num);
			break
	else:
		print(num, "is a prime number");
else:
	print(num, "is not a prime number");