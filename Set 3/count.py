'''
8. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
    - *Input*: A text file named "input.txt" with the content "Hello world"
    - *Output*: A text file named "output.txt" with the content "Number of words: 2"
'''


try:
    with open("/Set 3/input.txt",'r') as file:
        content = file.read()
    word_count = len(content.split())
    with open("output.txt",'w') as output_file:
        output_file.write(str(word_count))
        print(f"Number of words{word_count} words")

except FileNotFoundError:
        print(f"{input.txt} does not exist")    


