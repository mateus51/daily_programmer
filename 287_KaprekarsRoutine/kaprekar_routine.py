'''
/r/DailyProgrammer Challenge #287 - Kaprekar's Routine

Given a 4-digit number, return its largest digit

Bonus 1: Given a 4-digit number, return them in descending order
Bonus 2: Write a function that counts the number of iterations in Kaprekar's Routine, which is as follows.
Given a 4-digit number that has at least two different digits, take that number's descending digits, and subtract that number's ascending digits. For example, given 6589, you should take 9865 - 5689, which is 4176. Repeat this process with 4176 and you'll get 7641 - 1467, which is 6174.

'''

def largest_digit(number):
	separate_numbers = []
	
	if(number > 9999):
		print("The input has to be 4-digit or less")
		return

	for i in str(number):
		separate_numbers.append(int(i))
	
	print("largest_digit({0}) -> {1}".format(number, max(separate_numbers)))
	return int(max(separate_numbers))

print("/r/DailyProgrammer Challenge #287 - Kaprekar's Routine")

largest_digit(3456)
largest_digit(3222)
largest_digit(3574)
largest_digit(3333)
largest_digit(12345)
largest_digit(2000)
largest_digit(123)

