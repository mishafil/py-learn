import requests
req = requests.get('http://www.practicepython.org/assets/Training_01.txt')
text = [ln.split('/') for ln in req.text.split('\n')]
text.pop()
curritem, cnt = text[0][2], 0
for patharr in text :
	if patharr[2] == curritem :
		cnt += 1
	else :
		print(curritem, cnt)
		curritem = patharr[2]
		cnt = 1
print(curritem, cnt)

		
	
