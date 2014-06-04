from Tkinter import *

end = 4000000

def fib_seq():
	fibonacci = []
	base = 0
	next = 1
	counter = 0
	while next < end:
		fibonacci.append(next)
		previous = next
		next = base + next
		base = previous
		counter = counter + 1
	return fibonacci

		
fib_result = fib_seq()		

even_result = []
solution = 0
	
for i in fib_result:
	if i%2 == 0:
		even_result.append(i)
for e in even_result:
	solution = solution + e
		
	
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(solution)
r.destroy()    