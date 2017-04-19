def divisors(x) :
	return [y for y in range(1, x) if (x % y == 0)]
if __name__ == '__main__' :
	arg = int(input('Input a number: '))
	print(divisors(arg))
