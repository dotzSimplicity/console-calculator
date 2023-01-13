import math # This is needed for checking square root
import sys # This is needed for quitting the program

print("Hello World!")
print("It is time to do some Math!")
print("Note that this is Case-Sensetive.")
print(" ")

def withWhat_isnt_possible(): # This function gets called if withWhat isnt possible
    print("Either this feature isnt implemented or you wrote it wrong.")
    print("Console Calculator made by dotzSimplicity - Python Edition")
    print("This program has automatically exited.")
    sys.exit()

def is_withWhat_square_root(): # This function gets called if withWhat is "Square Root"
    print(math.sqrt(num1))
    print("Console Calculator made by dotzSimplicity - Python Edition")
    sys.exit()

possibleMath = ["Plus", "Times", "Division", "Minus", "Square Root"] # A now unneeded List, This was used for checking is withWhat is possible

num1 = int(input("First Number Please: ")) # Gets the First Number

withWhat = input("Plus, Times, Division or Minus, Square Root? ") # Gets the wanted method of math.

if withWhat == "Square Root": #This checks if withWhat is "Square Root", If so it calls a function
    is_withWhat_square_root()

num2 = int(input("Second Number Please: ")) # Gets the second number

if withWhat == "Plus": # If withWhat is "Plus", it adds num1 + num2, and so on
    print(num1 + num2)
elif withWhat == "Times":
    print(num1 * num2)
elif withWhat == "Division":
    print(num1 / num2)
elif withWhat == "Minus":
    print(num1 - num2)

print("bad Console Calculator made by dotzSimplicity - Python Edition")
