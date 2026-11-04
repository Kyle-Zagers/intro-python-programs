import math

# Variables for the Display Average menu option
sum_calc = 0.0
number_calc = 0
# Variables for the primary function and loop.
current_result = 0.0
exit_program = False
preserve = False  # Used to indicate that menu items do not need to be printed repeatedly.
# Operands. Defined outside of loop to be accessed by functions.
operand1 = 0.0
operand2 = 0.0


# Function which prints the menu depending on preserve and receives input from the user.
def print_menu():
    global preserve
    global current_result
    if not preserve:
        print(f"\nCurrent Result: {current_result}\n")
        print("Calculator Menu ")
        print("--------------- ")
        print("0. Exit Program "
              "\n1. Addition "
              "\n2. Subtraction "
              "\n3. Multiplication "
              "\n4. Division "
              "\n5. Exponentiation "
              "\n6. Logarithm "
              "\n7. Display Average ")
    return int(input("\nEnter Menu Selection: "))


# Gets the operands and assigns them as either a float or the result of the last calculation.
def get_operands():
    global current_result
    global operand1
    global operand2
    operand1 = input("Enter first operand: ")
    operand1 = current_result if operand1 == "RESULT" else float(operand1)
    operand2 = input("Enter second operand: ")
    operand2 = current_result if operand2 == "RESULT" else float(operand2)


# Prints the items for the Display Average menu selection.
def print_average():
    global sum_calc
    global number_calc
    print(f"\nSum of calculations: {sum_calc}")
    print(f"Number of calculations: {number_calc}")
    print(f"Average of calculations: {round(sum_calc/number_calc,2)}")  # Takes average & rounds to two decimal places.


# Primary loop for the calculator.
while not exit_program:
    selection = print_menu()  # Gets the selection and prints menu items.
    if 0 < selection < 7:  # Completes the math selections and resets the preserve variable.
        number_calc += 1
        get_operands()
        if selection == 1:
            current_result = operand1 + operand2
        if selection == 2:
            current_result = operand1 - operand2
        if selection == 3:
            current_result = operand1 * operand2
        if selection == 4:
            current_result = operand1 / operand2
        if selection == 5:
            current_result = operand1 ** operand2
        if selection == 6:
            current_result = math.log(operand2, operand1)
        sum_calc += current_result
        preserve = False

    if selection == 0:  # Prints the exit message and stops the loop from running again.
        print("\nThanks for using this calculator. Goodbye! ")
        exit_program = True

    if selection == 7:  # Executes print_average() and keeps print_menu() from printing the whole menu.
        preserve = True
        if number_calc > 0:
            print_average()
        elif number_calc == 0:  # Prints an error in the event that averages are requested during the first loop.
            print("\nError: No calculations yet to average! ")

    if selection < 0 or selection > 7:  # Prints error message if invalid input
        print("\nError: Invalid selection! ")
        preserve = True  # Keeps print_menu() from printing the whole menu.
