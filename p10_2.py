test_number = 200

def find_final_prime(final_number):
	prime_list = [2]
	next_num = 3
	while next_num < final_number:
		next_prime = find_prime(next_num, prime_list)
		if next_prime == True:
			prime_list.append(next_num)
		next_num = next_num + 1
	return prime_list
	
def find_prime(number, list):
	is_prime = True #True until proven false logic
	for i in range(0,len(list)): #Have defined range to go through the prime numbers
		if number%list[i] == 0:
			is_prime = False
			break
	return is_prime
	
prime_list = find_final_prime(100)

def double_minus_one(prime_list):
	list = []
	
	for i in prime_list:
		list.append(i+i-1)
	
	return list

def double_plus_one(prime_list):
	list = []
	
	for i in prime_list:
		list.append(i+i+1)
	
	return list
	
print find_final_prime(200)
print double_minus_one(prime_list)

	