'''
4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
    *Input*: [10, 20, 30, 40]
    *Output*: "Sum: 100, Average: 25.0"
'''

nums = input("enter no's :")

# Split the input string into a list of strings
number = nums.split()
# Convert the strings into integers
numbers = [int(x) for x in number]

sums = sum(numbers)
avg = sums/len(numbers)
print(f"Sum: {sums}, Average: {avg}")