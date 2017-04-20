beg, curr = 1,1
def fib(x) :
	global beg, curr
	for _ in range(0,x) :
		print(beg, end=' ')
		tmp = curr
		curr += beg
		beg = tmp
	beg, curr = 1,1
	print('\n')
	return None
# lim = int(input('Enter last fib index: '))
fib(1000)
	
