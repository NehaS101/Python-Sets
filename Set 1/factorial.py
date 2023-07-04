'''
8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
    *Input*: 5
    *Output*: "Factorial of 5 is 120."
'''


def fact(num):
    fac=1
    for i in range(1,num+1):
        fac = fac*i

    return fac

num=5
res=fact(num)
print(f"Factorial of {num} is {res}")