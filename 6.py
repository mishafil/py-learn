teststr = raw_input('Enter your string: ')
retVal = 'palindrome' if teststr == teststr[::-1] else 'not palindrome'
print(retVal)
