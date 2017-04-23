#!/usr/bin/env python3

def divisors(num) :
    cnt=0
    for x in range (1, num/2):
        if num % x == 0:
            cnt += 1
    return cnt + 1

if __name__ == '__main__' :
    num = int(input("Write a number"))
    print(divisors(num))
        
