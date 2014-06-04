series_start = 1000
prime = 999

def test_paladrome(number):
	raw_flip = [int(i) for i in str(number)]
	length = len(raw_flip)
	flipped_num = []
	count = 0
	for i in range(0,length):
		x = raw_flip.pop()
		flipped_num.append(x)
	inv_num = int(''.join(map(str,flipped_num)))
	if number == inv_num:
		return True
	else:
		return False
		
def process_series(number, prime):
	series_double = number+prime
	checked_series = []
	first_number = prime
	second_number = series_double - first_number
	while second_number < first_number:
		product = first_number * second_number
		checked_series.append([first_number,second_number,product])
		first_number = first_number - 1
		second_number = second_number + 1	
	return checked_series
	
def check_series(series_list):
	for i in series_list:
		x = test_paladrome(i[2])
		i.append(x)
	return series_list
		
def go_through_series(next_num, prime):
	next_list = process_series(next_num, prime)
	validation_list = check_series(next_list)
	total_trues = []
	for i in validation_list:
		if i[3] == True:
			total_trues.append(i)
	return total_trues
	
def find_largest_prime(series_start, prime):
	result = []
	while result == []:
		series_start = series_start - 1
		result = go_through_series(series_start, prime)
	print result

find_largest_prime(series_start, prime)	
