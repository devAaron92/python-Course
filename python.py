#Please write a program which asks the user to type in a limit. 
#The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
#until the sum is at least equal to the limit set by the user. 
#The program should function as follows:

limit = int(input("Please enter a limit: "))
var = 0
sum = 0


while True:
        var += 1
        sum += var
        print(sum)
        if sum >= limit:
                break 