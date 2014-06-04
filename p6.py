final_number = 100 #Number we're going to in order to test the Sum Square Difference

def find_sum_of_squares(number):
	sos = 0 #Stands for 'sum of squares'
	for i in range(0,number +1):
		sos = sos + (i * i)
	return sos

def find_square_of_sums(number):
	sum = 0 #Stands for 'square of sum'
	for i in range(0,number +1):
		sum = sum + i
	return sum * sum
	
def find_difference(number):
	sum_of_squares = find_sum_of_squares(number)
	square_of_sums = find_square_of_sums(number)
	return square_of_sums - sum_of_squares

print find_difference(final_number)	