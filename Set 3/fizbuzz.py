'''
7. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
    - *Input*: None
    - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."
'''

num=100
res=[]
for i in range(num):
    if i%3==0:
        i="Fuzz"
    elif i%5==0:
        i="Buzz"
    elif i%3==0 and i%5==0:
        i="FizzBuzz"
    print(i)            