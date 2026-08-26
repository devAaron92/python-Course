#Please write a program which asks the user to type in a string and a single character. 
#The program then prints the first three character slice which begins with the character specified by the user. 
#You may assume the input string is at least three characters long. The program must print out three characters, or else nothing.

#Pay special attention to when there are less than two characters left in the string after the first occurrence of the character looked for. 
#In that case nothing should be printed out, and there should not be any indexing errors when executing the program.

#Please make an extended version of the previous program, 
#which prints out all the substrings which are at least three characters long, 
#and which begin with the character specified by the user. You may assume the input string is at least three characters long.

stringy = input("Please enter a string: ")
char = input("Please Enter a char")
start = 0
index = stringy.find(char,0)

#index2 = stringy.find(char, index + 1)
#index3 = stringy.find(char, index2 + 1)
if index == -1:
    print("string not found")

elif len(stringy[index: index - 1]) < 2:
    print(" ")
else: 
    print(stringy[index: index + 3])
    print(stringy[index2: index + 3])
    print(stringy[index3: index + 3])


