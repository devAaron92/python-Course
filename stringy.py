#Please write a program which asks the user for a string 
# and then prints it out so that exactly 20 characters are displayed. 
#If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
#You may assume the input string is at most 20 characters long.


stringy = input("Please enter a string: ")
char = "*"
lengthOfString = len(stringy)
n = 0
difference = 20 - lengthOfString
n = 0
padding = 0

while n < 20 - lengthOfString:
    n += 1
    padding = n

print((n * char) + stringy)