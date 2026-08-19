#Please write a program which asks the user to type in an upper limit. 
#The program then prints out numbers so that each subsequent number is the previous one doubled, 
#starting from the number 1. That is, the program prints out powers of two in order.

#The execution of the program finishes when the next number to be printed would be greater than the limit set by the user.
#No numbers greater than the limit should be printed.

## Please change the program from the previous exercise so that the user gets to input 
#also the base which is multiplied (in the previous program the base was always 2).

upperLmit = int(input("Please enter in an upper Limit: "))
base = 1


while True:
    print(base)
    base *= 2
    if base > upperLmit:
        break