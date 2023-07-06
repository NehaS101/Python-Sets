'''
9. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
    - *Input*: 5, 0
    - *Output*: "Cannot divide by zero."
'''

num1=5
num2=0

try:
    res = num1/num2
    print(res)
except ZeroDivisionError:
    print("Cannot divide by zero")    