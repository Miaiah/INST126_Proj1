# import the math module in order to use sqrt()
import math


# function for addition
def addition(num1, num2):
    add = num1 + num2
    return add


# function of subtraction
def subtraction(num1, num2):
    sub = num1 - num2
    return sub


# function of multiplication
def multiplication(num1, num2):
    mul = num1 * num2
    return mul


# function of division
def division(num1, num2):
    div = num1 / num2
    return div


# function of modulo
def modulo(num1, num2):
    mod = num1 % num2
    return mod


# function of exponentiation
def exponentiation(num1, num2):
    exp = num1 ** num2
    return exp


# function of Square Root
def squareroot(num1):
    squ = math.sqrt(num1)
    return squ


# function of Floor Division
def floordivision(num1, num2):
    flo = num1 // num2
    return flo

# while loop to allow user to reenter values
while 1 > 0:
    # display the types of operations
    print("Your Operation Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    print("6. Exponentiation")
    print("7. Squareroot")
    print("8. Floor Division")
    print("9. End")
    # ask user to input the operation their want the program to perform
    operation = input("\nChoose an operation(enter letters plz): ")

    # run an addition operation when user choose Addition
    if operation == "Addition" or operation == "addition" or operation == "ADDITION":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = addition(var1, var2)
        print("The answer is: " + str(final_var) + "\n")

    # run a subtraction operation when user choose Subtraction
    elif operation == "Subtraction" or operation == "subtraction" or operation == "SUBTRACTION":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = subtraction(var1, var2)
        print("The answer is: " + str(final_var) + "\n")

    # run a multiplication operation when user choose Multiplication
    elif operation == "Multiplication" or operation == "multiplication" or operation == "MULTIPLICATION":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = multiplication(var1, var2)
        print("The answer is: " + str(final_var) + "\n")

    # run a division operation when user choose Division
    elif operation == "Division" or operation == "division" or operation == "DIVISION":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = division(var1, var2)
        print("The answer is: " + str(round(final_var, 2)) + "\n")

    # run a modulo operation when user choose Modulo
    elif operation == "Modulo" or operation == "modulo" or operation == "MODULO":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = modulo(var1, var2)
        print("The answer is: " + str(final_var) + "\n")

    # run an exponentiation operation when user choose Exponentiation
    elif operation == "Exponentiation" or operation == "exponentiation" or operation == "EXPONENTIATION":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = exponentiation(var1, var2)
        print("The answer is: " + str(final_var) + "\n")

    # run a Square Root operation when user choose Squareroot
    elif operation == "Squareroot" or operation == "squareroot" or operation == "SQUAREROOT":
        var = float(input("Enter your value: "))
        final_var = squareroot(var)
        print("The answer is: " + str(final_var) + "\n")

    # run a Floor Division operation when user choose Floor Division
    elif operation == "Floor Division" or operation == "floor division" or operation == "floordivision":
        var1 = float(input("Enter your first value: "))
        var2 = float(input("Enter your second value: "))
        final_var = floordivision(var1, var2)
        print("The answer is: " + str(final_var) + "\n")

    # stop the program when user choose to stop calculating
    elif operation == "End" or operation == "end" or operation == "END":
        print("See you!")
        break

    # display an error message when user input something other than the offered options
    else:
        print("Invalid input, please try again.\n")
