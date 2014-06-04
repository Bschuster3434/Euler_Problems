import time
import math
start_time = time.time()

number = 1000
final_prime = 1000 #Expected Number of Primes Needed

def find_all_primes(final_number):
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
	
prime_list = find_all_primes(final_prime)

def find_num_divisors(number, prime_list):
	prime_divisors = [] #Finds the list of prime divisors
	
	sqrt = int(math.floor(number ** 0.5)) #There are no prime divisors below sqrt(n)
	sac_number = number #sacraficial number
	
	prime_pos = 0 #Iterator for list
	prime_num = 2 #First Prime #
	
	while prime_num <= sqrt:
		if sac_number%prime_num == 0:
			prime_divisors.append(prime_num)
			sac_number = sac_number/prime_num
		else:
			prime_pos = prime_pos + 1
			prime_num = prime_list[prime_pos]
	
	return prime_divisors

print find_num_divisors(number, prime_list)	
	
print time.time() - start_time, "seconds"