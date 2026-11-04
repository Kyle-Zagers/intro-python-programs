num1 = float(input("Enter first operand: "))  # asking and getting input for the first operand
num2 = float(input("Enter second operand: "))  # asking and getting input for the second operand

print("\nCalculator Menu \n--------------- ")
print("1. Addition ")
print("2. Subtraction ")
print("3. Multiplication ")
print("4. Division ")
# these print statements are to show the menu

operation = int(input("\nWhich operation do you want to perform? "))  # asks and gets the operation option


def result(number):
    print(f"The result of the operation is {number}. Goodbye! ")
# this function returns the result of the operation
# I made a function as to not have repeated code


if operation == 1:
    result(num1 + num2)
elif operation == 2:
    result(num1 - num2)
elif operation == 3:
    result(num1 * num2)
elif operation == 4:
    result(num1 / num2)
else:  # error case
    print("\nError: Invalid selection! Terminating program. ")
# completes the inputted operation and gives the result to the result function
# done using elif to eliminate unneeded conditions for the error case
