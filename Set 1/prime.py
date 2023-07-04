'''
7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
    *Input*: 13
    *Output*: "13 is a prime number."
'''

import math
def check(num):
    if num<2:
        return False
    prime=True
    for i in range(2,int(math.sqrt(num))+1) :
        if num%i==0:
            prime=False
            break
    return prime
num=13
output=check(num)
if output==True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a prime number")
