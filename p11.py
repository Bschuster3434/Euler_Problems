import time
import urllib2
start_time = time.time()

website = "http://projecteuler.net/problem=11"

def grab_relevant_code(website):
	source = urllib2.urlopen(website)
	list = source.readlines()
	full_list_string = ''.join(list)
	
	string_start = "<p style=\"font-family:courier new;text-align:center;font-size:10pt;\">"
	string_end = "</p>"
	
	start_loc = full_list_string.find(string_start) #Finds the location in string where first unique identifier exists
	half_list_string = full_list_string[start_loc + len(string_start):] #Takes full string and shortens it to the beginning
	
	end_loc = half_list_string.find(string_end) #Finds end location in new string
	list_string = half_list_string[:end_loc] #Cuts down to just the relevant string
	
	return list_string
	
def clean_html(string):
	
	d_1 = ["<br />", "<span style=\"color:#ff0000;\"><b>", "</b></span>", "\r"] #defect list
	
	for i in d_1:
		string = string.replace(i, '')
	
	return string
			

def parse_into_lines(string):
	rows = [] #String of strings
	
	parse = '\n'
	
	while len(string) > 0:
		next_end = string.find(parse)
		rows.append(string[:next_end])
		string = string[next_end + len(parse):]
	
	return rows[1:] #Gets rid of the first empty row

def parse_rows_into_lists(list):
	new_rows = []
	parse = ' '
	
	for i in list:
		listed_row = []
		while len(i) > 0:
			next_break = i.find(parse)
			if next_break == -1:
				listed_row.append(i)
				i = ''
			else:
				listed_row.append(i[:next_break])
				i = i[next_break + len(parse):]
		new_rows.append(listed_row)
	
	return new_rows


def make_vertical_list(horizontal_numbers): #Take the number list and make it vertical
	vert_rows = []
	
	while len(horizontal_numbers[0]) > 0:
		next_row = []
		for i in range(0,len(horizontal_numbers)):
			next_row.append(horizontal_numbers[i].pop(0))
		vert_rows.append(next_row)
	
	return vert_rows
	
def make_diagonal_list(horizontal_numbers, direction): #starts at the top left and cascades the list going to the bottom right

	diag = [] #List to Return
	vertical_length = len(horizontal_numbers) #Finding vertical size of matrix
	horizontal_length = len(horizontal_numbers[0]) #Finding horizontal size of matrix
	
	#Starts first position of the matrix, then iterates down the vertical side, then the horizontal size	

	if direction == "R": #Moves Top Left to Bottom Right
		start_horizontal_pos = 0
		start_vertical_pos = 0	
	
		while start_horizontal_pos < horizontal_length: #Should iterate through every row
			next_diag = []
		
			next_horizontal = start_horizontal_pos
			next_vertical = start_vertical_pos
		
			while next_vertical >= 0 and next_horizontal < horizontal_length: #Stops after we go through the top of the matrix	
				find_row = horizontal_numbers[next_horizontal] #Finds the specific row
				find_number = find_row[next_vertical] #Finds the exact number in the series
				next_diag.append(find_number)
			
				next_vertical = next_vertical - 1
				next_horizontal = next_horizontal + 1
			
			diag.append(next_diag) #append the new list to the diag
		
			if start_vertical_pos < vertical_length - 1:
				start_vertical_pos = start_vertical_pos + 1

			else:
				start_horizontal_pos = start_horizontal_pos + 1
		
	elif direction == "L": # Moves Top Right to Bottom Left
		start_horizontal_pos = 0
		start_vertical_pos = vertical_length - 1	
	
		while start_vertical_pos >= 0: #Should iterate through every row
			next_diag = []
		
			next_horizontal = start_horizontal_pos
			next_vertical = start_vertical_pos
			
		
			while next_horizontal >= 0 and next_vertical >=0 : #Stops after we go through the top of the matrix	
				find_row = horizontal_numbers[next_horizontal] #Finds the specific row
				find_number = find_row[next_vertical] #Finds the exact number in the series
				next_diag.append(find_number)
			
				next_vertical = next_vertical - 1
				next_horizontal = next_horizontal - 1
			
			diag.append(next_diag) #append the new list to the diag
		
			if start_horizontal_pos < horizontal_length - 1:
				start_horizontal_pos = start_horizontal_pos + 1

			else:
				start_vertical_pos = start_vertical_pos - 1
				
	return diag
	
def list_of_chunks(chunk_list, original_list):
	number = 4 #Chunk Length
	
	for i in original_list:
		start_pos = 0

		list_length = len(i) #Length of individual list
		
		while (start_pos + number) <= list_length:
			next_chunk = i[start_pos:start_pos + number]
			chunk_list.append(next_chunk)
			start_pos = start_pos + 1
			
	return chunk_list
	
def add_product(chunk_list):
	product_list = []
	
	for i in chunk_list:
		product = 1
		for e in i:
			product = product * int(e)
		product_list.append([i, product])
	
	return product_list
	
def return_greatest_product(list):
	greatest_product = [[],1]
	
	for i in list:
		if i[1] > greatest_product[1]:
			greatest_product = i
			
	return greatest_product
	
	
	
def main(website):	#Grabs the numbers as seen on problem 8
	######### Grab Horizontal List
	code = grab_relevant_code(website)
	new_code = clean_html(code)
	rows = parse_into_lines(new_code)
	listed_rows = parse_rows_into_lists(rows) #For Horizontal + Diagonals
	list_rows_1 = parse_rows_into_lists(rows) #For Vertical
	
	#Groups of lists added together	
	horizontals = listed_rows 
	verticals = make_vertical_list(list_rows_1)
	right_diagonal = make_diagonal_list(listed_rows, "R")
	left_diagonal = make_diagonal_list(listed_rows, "L")
	
	#Empty Chunk List
	chunk_list = []
	#Cuts list into correct chunks
	chunk_list = list_of_chunks(chunk_list, horizontals)
	chunk_list = list_of_chunks(chunk_list, verticals)
	chunk_list = list_of_chunks(chunk_list, right_diagonal)
	chunk_list = list_of_chunks(chunk_list, left_diagonal)
	
	#Now adding the product to the list
	product_list = add_product(chunk_list)
	
	#Finds the greatest product and returns that list
	greatest_product = return_greatest_product(product_list)
	
	return greatest_product


	
print main(website)
print time.time() - start_time, "seconds"