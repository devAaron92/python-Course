#Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. 
#If the strings are of equal length, the program should print out "The strings are equally long".
#Some examples of expected behaviour:

stringy1 = input("Please Enter a string")

stringy2 = input("Please enter a second string")

if len(stringy1) == len(stringy2):
    print("The strings are equal")

elif len(stringy1) > len(stringy2):
    print(stringy1)

else:
    print(stringy2)