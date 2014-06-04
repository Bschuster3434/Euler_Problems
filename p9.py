big_limit = 1000



def get_product(limit):
	next_a = 1
	is_pythagorus = [0,0,0]
	
	while is_pythagorus == [0, 0, 0]:
		is_pythagorus = iterate_a_equals_set(next_a, limit)
		next_a = next_a + 1
	
	print "THE PRODUCT OF THE NUMBERS IS " + str((is_pythagorus[0] * is_pythagorus[1] * is_pythagorus[2]))
		




def iterate_a_equals_set(a, limit): #Given first a, iterate and test the rest of the set
	next_b = a + 1 #b starts at a+1
	next_c = limit - a - next_b #c starts at limit minus the first two variables
	
	while next_c > next_b: #Stops due to parameter constraints on this set
		is_pythagorus = test_set_equal(a, next_b, next_c)
		if is_pythagorus == True:
			break
		next_b = next_b + 1
		next_c = next_c - 1 #iteration of the series, b goes up, c goes down, until they meet or cross paths
	
	if is_pythagorus == True:
		return [a, next_b, next_c]
	else:
		return [0, 0, 0]
			
	

def test_set_equal(a, b, c): #tests the Pythagorean theory
	result = False
	left = (a * a) + (b * b)
	right = (c * c)
	if left == right:
		result = True
	return result
	

get_product(big_limit)