final_divisor = 20 #DO NOT RUN OVER 20
# Code to find the prime number, given a final number
# I'm so damn proud of it that I'm not going to erase it
# And there's not a god damn thing you can do about it

#def find_primes(number):
#	prime_list = []
#	for i in range(2,number + 1):
#		e = i - 1
#		prime = True
#		while e > 1:
#			if i%e == 0:
#				prime = False
#			e = e - 1
#		if prime == True:
#			prime_list.append(i)
#	return prime_list

def check_number(number, final_divisor):
	totally_divisible = True #Running a 'True until shown False' analysis
	next_check = 2 #Starts with the first number after one, since it's a wasted calculation
	while totally_divisible == True and next_check <= final_divisor: #Meant to not go over the divisor number, but also stops if a calculation turns out to be wrong. Saves calc time.
		if number%next_check != 0:
			totally_divisible = False
		next_check = next_check + 1
	return totally_divisible #Returns binary
	
def check_set(final_divisor):
	next_number = final_divisor + 1 #Starting with the next number after the final_divisor
	number_found = 0 #Zero because no number was found in the beginning
	while 1==1:
		num_check = check_number(next_number, final_divisor)
		if num_check == True:
			number_found = next_number
			break
		next_number = next_number + 1
	return number_found
		
print check_set(final_divisor) #start program