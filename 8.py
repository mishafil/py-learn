playing = True
polozhnyak = { 'Rock' : 'Scissors',
		'Scissors' : 'Paper',
		'Paper' : 'Rock' }
def testinp(item) :
	return True if item in polozhnyak else False;
while playing :
	pl1, pl2 = input('Player1`s choice: '), input('Player2`s choice: ')
	if testinp(pl1) == False or testinp(pl2) == False :
		print('Wrong item entered!')	
	elif pl1 == pl2 :
		print('No winner!')
	elif polozhnyak[pl1] == pl2 :
		print('Player1 Won!')
	elif polozhnyak[pl2] == pl1 :
		print('Player2 Won!')
	print('Wanna play one more time? (y/n)')
	ans = input()
	playing = True if ans == 'y' else False
print('Nice game!')
	
