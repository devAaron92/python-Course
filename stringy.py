#Please write a program which asks the user to type in a string. 
#The program then prints out all the substrings which begin with the first character, 
#from the shortest to the longest. Have a look at the example below.

stringy = input("Enter a string: ")
length = len(stringy)
n = 0
while n < length:
    print(stringy[0:n + 1])
    n += 1