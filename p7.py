place = 10001

def find_prime(number, list):
	is_prime = True #True until proven false logic
	for i in range(0,len(list)): #Have defined range to go through the prime numbers
		if number%list[i] == 0:
			is_prime = False
			break
	if is_prime == True:
		list.append(number)
	return list
		

def find_final_prime(place):
	prime_list = [2]
	next_num = 3
	while len(prime_list) < place:
		find_prime(next_num, prime_list)
		next_num = next_num + 1
	return prime_list[place-1]
	
print find_final_prime(place)