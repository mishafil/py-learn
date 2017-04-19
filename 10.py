a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a :
	if a.count(x) > 1 :
		a.pop(a.index(x))
print([x for x in a if x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]])
