'''
6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
    *Input*: "Hello"
    *Output*: "Number of vowels: 2"
'''

def vowel(string):
    vowels="aeiouAEIOU"
    count=0
    for key in string:
        if key in vowels:
            count+=1
    return count

string="Hello"
result=vowel(string)
print(result)