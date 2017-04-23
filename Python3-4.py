#!/usr/bin/env python3
num = int(input("Write a number"))
cnt=0
for x in range (1, num/2):
    if num % x == 0:
        cnt += 1
return cnt + 1        
        
