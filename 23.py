import requests
primes = requests.get('http://www.practicepython.org/assets/primenumbers.txt')
happys = requests.get('http://www.practicepython.org/assets/happynumbers.txt')
overlap = [x for x in primes.text.split('\n') if x in happys.text.split('\n')]
print(overlap)
