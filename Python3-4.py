#!/usr/bin/env python3
num = int(input("Print number: "))
for x in range(1, num/2):
        while ( num % x == 0 ):
            print(x,num) 
            

