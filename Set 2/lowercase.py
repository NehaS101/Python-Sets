'''
Problem4: Arrange string characters such that lowercase letters should come first**

Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

**Given**
str1 = PyNaTive

**Expected Output**
yaivePNT

'''

str1 = "PyNaTive"
s2=""
s3=""
for i in str1:
    if i.islower():
        s2+=i
    else:
        s3+=i

print(s2+s3)            