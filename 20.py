def bin_search(sequence, searched) :
	if len(sequence) == 1 :
		return True if sequence[0] == searched else False
	else :
		middle = sequence[len(sequence)//2]
		return bin_search(sequence[:len(sequence)//2], searched) if searched < middle else bin_search(sequence[len(sequence)//2:], searched)

if __name__ == '__main__' :
	print(bin_search([0,1,3,5,6,8,9], int(input('Enter a num: '))))
