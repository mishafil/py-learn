playing = True
da_rules = { 'Rock' : 'Scissors',
		'Scissors' : 'Paper',
		'Paper' : 'Rock' }
while playing :
	pl1, pl2 = input('Player1`s choice: '), input('Player2`s choice: ')
	if pl1 not in da_rules or pl2 not in da_rules :
		print('Wrong item entered!')	
	elif pl1 == pl2 :
		print('No winner!')
	elif da_rules[pl1] == pl2 :
		print('Player1 Won!')
	elif da_rules[pl2] == pl1 :
		print('Player2 Won!')
	ans = input('Wanna play one more time? (y/n) ')
	playing = True if ans == 'y' else False
print('Nice game!')
	
