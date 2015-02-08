def fib():
	a = 0
	b = 1
	for i in range(500):
		print a 
		a, b = b, a + b

print fib()
