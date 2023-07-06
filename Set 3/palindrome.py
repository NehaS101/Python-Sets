'''
4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
    - *Input*: "madam"
    - *Output*: "The word madam is a palindrome."
'''
str1="madam"
str2=""

for i in reversed(str1):
    str2 += i

if(str1==str2):
    print(f"The word {str1} is a palindrome")   