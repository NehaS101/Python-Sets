'''
9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
    *Input*: 5
    *Output*: "[0, 1, 1, 2, 3]"
'''
def fibonacci(num):
 fibon =[0,1]

 if num <= 2:
  return fibon[:num]
 
 while len(fibon) < num:
  next = fibon[-1]+fibon[-2]
  fibon.append(next)

  return fibon
 
num=4
res=fibonacci(num)
print(res) 