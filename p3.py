from Tkinter import *

base = 600851475143
factors = [1]
factor_counter = 1

def factors_multiple(factors):
	multiple = 1
	for i in factors:
		multiple = multiple * i
	return multiple

factors_multi_result = factors_multiple(factors)
		

while factors_multi_result != base:
	factor_counter = factor_counter + 1
	if base%factor_counter == 0:
		run = True
		while run == True:
			factors.append(factor_counter)
			base = base/factor_counter
			if base%factor_counter != 0:
				run = False


r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(factors[-1])
r.destroy() 
