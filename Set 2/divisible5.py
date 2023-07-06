'''
### Problem **2: Display numbers from a list using loop**

Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

- The number must be divisible by five
- If the number is greater than 150, then skip it and move to the next number
- If the number is greater than 500, then stop the loop

**Given**

numbers = [12, 75, 150, 180, 145, 525, 50]

**Expected output**

75
150
145

'''
numbers = [12, 75, 150, 180, 145,525,50]
for i in numbers:
    if i%5==0 and i<=150:
        print (i)
    elif i >500:
        break    