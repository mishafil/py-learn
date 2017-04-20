from random import randint

def genPswd(length) :
	'''Generates password of specified length'''
	pswd = str()
	for _ in range(0, length) :
		pswd += chr(randint(33, 126))
	return pswd

if __name__ == '__main__' :
	print(genPswd(64))
