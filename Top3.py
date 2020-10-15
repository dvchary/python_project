# Python Program to find the largest number among the three input numbers

# Change the values of Num 1, Num 2 and Num 3 for a different results

#num1 = 10
#num2 = 14
#num3 = 15

# uncomment following lines to take three numbers from user

num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))
num3 = float(input("Enter the 3rd Number: "))

if (num1 >= num2) and (num1 >= num3):
	largest = num1
elif (num2 >= num1) and (num2 >= num3):
	largest = num2
else:
	largest = num3
print("The Largest Number is ", largest)
	