import urllib2

website = "http://projecteuler.net/problem=8"

def return_greatest_product(website):
	source = urllib2.urlopen(website)
	list = source.readlines()
	full_list_string = ''.join(list)
	
	string_start = "<p style='font-family:courier new;font-size:10pt;text-align:center;'>"
	string_end = "</p>"
	
	start_loc = full_list_string.find(string_start) #Finds the location in string where first unique identifier exists
	half_list_string = full_list_string[start_loc + len(string_start):] #Takes full string and shortens it to the beginning
	
	end_loc = half_list_string.find(string_end) #Finds end location in new string
	list_string = half_list_string[:end_loc] #Cuts down to just the relevant string
	
	number_string = grab_number_list(list_string) #Output is single string with 1000 digits
	
	digit_list = parse_number_to_length(number_string) #Output is list of strings with 5 digits each
	
	non_zero_digit_list = remove_zero_case(digit_list) #Output is same list as digit_list, minus the zero cases
	
	product_digit_list = add_product(non_zero_digit_list) #Output is same list as non_zero_digit_list, with each entry having an appended product
	
	largest_product = find_larget_product(product_digit_list)
	
	return largest_product
	
def grab_number_list(string): # Grabs the raw numbers from the string and formats them as one number
	number_list = []
	parse = "<br />"
	
	while string.find(parse) != -1:
		next_end_loc = string.find(parse)
		number_list.append(string[1:next_end_loc])
		next_start_loc = next_end_loc + len(parse)
		string = string[next_start_loc:]
	
	final_number = ''.join(number_list)
		
	return final_number

	
def parse_number_to_length(number_string):
	digit_list = []
	length = 5
	
	while len(number_string) >= 5:
		digit_list.append(number_string[0:length])
		number_string = number_string[1:]
	
	return digit_list
	
def remove_zero_case(digit_list): #Remove all strings where product equals 0
	non_zero_digit_list = []
	
	for i in digit_list:
		find_zero = i.find('0')
		if find_zero == -1:
			non_zero_digit_list.append(i)
	
	return non_zero_digit_list
	
def add_product(digit_list): #turns number into a two place list and adds product into the '1' list place
	dig_pro_list = []
	
	for i in digit_list:
		product = 1
		product = int(i[0]) * int(i[1]) * int(i[2]) * int(i[3]) * int(i[4])
		dig_pro_list.append([i, product])
	
	return dig_pro_list	
	
def find_larget_product(product_list):
	largest_product_pair = ['', 0]
	
	for i in product_list:
		if i[1] > largest_product_pair[1]:
			largest_product_pair = i
	return largest_product_pair
	
	
	
	
print return_greatest_product(website)
	
	
	
	

	
