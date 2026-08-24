#Please write a program which asks the user for a string. 
#The program then prints out a message based on whether the second character and the second to last character are the same or not. 
#See the examples below.


stringy = input("please enter a string: ")

secondToLast = len(stringy) -2 

if stringy[1] == stringy[secondToLast]:
    print("The second and the second to last characters are the same")

else:
    print("The second and the second to last characters are different")
