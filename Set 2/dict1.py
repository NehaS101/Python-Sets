'''
Problem8: Initialize dictionary with default values

In Python, we can initialize the keys with the same values.

**Given**
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

**Expected output:**
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

'''

employees = ["Kelly", "Emma"]
defaults = {"designation": "Developer", "salary":8000}

res = {x:defaults for x in employees}
print(res)