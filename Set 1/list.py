'''
3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
    *Input*: None
    *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."
'''

#create a list of numbers
nums=list(range(1,10+1))
print(nums)

#adding no
nums.append(9)
print(nums)

#removing a no
nums.remove(1)
print(nums)

#sort the list
nums.sort()
print(nums)