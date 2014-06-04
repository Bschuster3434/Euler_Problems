from Tkinter import *

multiples = []
exclusive_end = 1000
result = 0

for i in range(0,exclusive_end):
	if i%3 == 0 or i%5 == 0:
		multiples.append(i)
		

for e in multiples:
	result = result + e


r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(result)
r.destroy()    