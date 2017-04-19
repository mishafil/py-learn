from random import randint
inp = ''
while True :
	guess = randint(1, 9)
	inp = input("Enter num or type 'exit': ")
	if inp == 'exit' : 
		break
	else :
		inpInt = int(inp)
		if inpInt == guess :
			print('Nice!')
		elif inpInt < guess :
			print('Too small')
		elif inpInt > guess :
			print('Too big')

