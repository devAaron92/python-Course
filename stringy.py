#Please write a program which asks the user for strings using a loop. 
# The program prints out each string underlined as shown in the examples below. 
# The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.


while True:
   stringy = input("Please Enter a string: ")
   print(stringy)
   underline = len(stringy) * '_'
   print(underline)
   if stringy == "":
      break