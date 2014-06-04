primes = [2]
final_number = 2000000

number_range = range(3, final_number + 1, 2)

for i in number_range:
        
    root_i = i ** 0.5

    for p in primes:       
        
        if p > root_i: 
            primes.append(i)      
            break

        if i % p == 0:
            break
 

sum = 0
for i in primes:
	sum = sum + i

print sum
