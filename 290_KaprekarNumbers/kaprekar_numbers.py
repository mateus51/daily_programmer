'''
/r/DailyProgrammer Challenge #290 - Kaprekar's Number

'''

def kaprekar_number(n):
	squared = str(n ** 2)

	# This allows for slices in every single position
	# Such as: 2025 -> 2|025, 20|25, 202|5, because the index keeps increasing
	for i in range(len(squared) - 1):
		a = int(squared[:i+1])
		b = int(squared[i+1:])

		if((a + b == n) and (a != 0) and (b != 0)):
			return True

	return False

def find_kaprekar(lower, upper):
	kap_list = list(filter(kaprekar_number, range(lower, upper)))
	print(kap_list)
	return kap_list

lower, upper = map(int, input().split())

find_kaprekar(lower, upper)