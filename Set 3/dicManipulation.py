'''
2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
    - *Input*: Add "John": 25, Update "John": 26, Delete "John"
    - *Output*: "{}, {'John': 26}, {}"
'''

def add(dic,name,age):
    dic[name] = age

def update(dic,name,age):
    if name in dic:
        dic[name] = age

def delete(dic,name):
    if name in dic:
        del dic[name]   

data = {}
add(data,"John",25)
print(data)

update(data,"John",26)
print(data)

delete(data,"John")
print(data)
