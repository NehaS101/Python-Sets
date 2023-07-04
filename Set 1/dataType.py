'''
2. **Data Type Play**: Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
    *Input*: None
    *Output*: "Type of variable1: <class 'int'>, value: 10..."
'''

#integer 
age=5
print(f"{type(age)}, value: {age}" )

#float
temp=25.8
print(f"{type(temp)}, value: {temp}")

#string
name="neha solanki"
print(f"{type(name)}, value: {name}")

#boolean
is_hot=True
print(f"{type(is_hot)}, value: {is_hot}")

#list
nums = [1,2,3,4,5,6,7]
print(f"{type(nums)}, values: {nums}")

#dictionary
obj = {"name":"neha","age":5}
print(f"{type(obj)}, value: {obj}")

#tuple
tuples = (0,1,2,3)
print(f"{type(tuples)}, value: {tuples}")

#sets
set={2,4,5,8,9}
print(f"{type(set)}, value: {set}")