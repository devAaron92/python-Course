#Please write a program which asks the user for a string and
#then prints out a frame of * characters with the word in the centre. 
#The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.
#If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.


stringy = input("please enter a string: ")
width = (28 - len(stringy)) // 2
print(30 * "*")
print("*" +(width * " ") + (stringy) + (" " * width) + "*")
print(30 * "*")
#print(" " * difference )

print(width)

#stringy = input("Please enter a string: ")
#char = "*"
#lengthOfString = len(stringy)
#n = 0
#difference = 20 - lengthOfString
#n = 0
#padding = 0

#while n < 20 - lengthOfString:
 #   n += 1
  #  padding = n

#rint((n * char) + stringy)