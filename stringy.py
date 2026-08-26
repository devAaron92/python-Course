#Please write a program which asks the user to type in a string. 
#The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
#Have a look at the example below.

stringy = input("Enter a string: ")
length = len(stringy)
n = length 
while n > 0:
    print(stringy[n-1:length])
    n -= 1
   
