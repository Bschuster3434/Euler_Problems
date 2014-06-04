import math
start_time = time.time()

final_number = 1000000#Answer asks for below 2,000,000, so this is not inclusive

def find_final_prime(final_number):
	prime_list = [2]
	next_num = 3
	while next_num < final_number:
		next_prime = find_prime(next_num, prime_list)
		if next_prime == True:
			prime_list.append(next_num)
		next_num = next_num + 2
	return prime_list
	
def find_prime(number, list):
	is_prime = True #True until proven false logic
	square = number ** 0.5
	for i in range(0,int(math.floor(square))): #Have defined range to go through the prime numbers
		if number%list[i] == 0:
			is_prime = False
			break
	return is_prime