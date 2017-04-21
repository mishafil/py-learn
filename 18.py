from random import randint
import sys #use 'demo' argument to autoplay
print('Welcome to the Cows and Bulls Game!\nEnter a number: ')

def cowbull(guess) :
	rand = randint(1000, 9999)
	cows, bulls = 0,0
	for i in range(0,4) :
		if str(guess)[i] in str(rand) :
			if str(guess)[i] == str(rand)[i] :
				cows += 1
			else :
				bulls += 1
	return (cows, bulls)

def printRes(result) :
	cw = 'cow' if result[0] == 1 else 'cows'
	bl = 'bull' if result[1] == 1 else 'bulls'
	print(result[0], cw + ',', result[1], bl)
	return None

playing, autoplay = True, True if 'demo' in str(sys.argv) else False
counter = 0
while playing == True :
	guess = int(input('>>> ')) if autoplay == False else randint(1000, 9999) - 421
	if guess > 9999 or guess < 1000 :
		print('Number must be between 1000 and 9999')
		continue
	result = cowbull(guess)
	printRes(result)
	counter += 1
	playing = False if result[0] == 4 else True
print('Nice game! It took you {} attempts to win.'.format(counter))
