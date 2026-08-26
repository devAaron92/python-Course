#Please write a program which asks the user to input a string. 
# The program then prints out different messages if the string contains any of the vowels a, e or o.
#You may assume the input will be in lowercase entirely. Have a look at the examples below.

substring = input("Please enter a string: ")

while True:
    if 'a' in substring:
        print("found a") 
        if 'e' in substring:
            print("found e")    
        if 'i' in substring:
            print("found i") 

        if 'o' in substring:
            print("found o") 
        if 'u' in substring:
            print("found u")    
 