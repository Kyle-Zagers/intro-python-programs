def menu(option):  # Creates the menu and receives menu input.
    print("Decoding Menu")
    print("-" * 13)
    print("1. Decode hexadecimal \n2. Decode binary \n3. Convert binary to hexadecimal \n4. Quit ")
    result = input("\nPlease enter an option: ") if option else None
    return input("Please enter the numeric string to convert: ") if result != "4" else None, result


def hex_char_decode(digit):  # Converts a hexadecimal digit into a decimal number.
    result = 0
    if "9" >= digit >= "0":
        result = int(digit)
    else:
        result = (ord(digit.lower()) % ord('a')) + 10  # Uses unicode values to get value.
    return result


def hex_string_decode(hex):  # Converts from hexadecimal to decimal.
    hex = hex[2:len(hex)] if len(hex) > 2 and hex[1] == 'x' else hex  # Condition for prefix.
    hex_list = list(hex)
    result = 0
    for i in range(0, len(hex_list)):  # Basic hexadecimal to decimal conversion.
        result += hex_char_decode(hex_list[len(hex_list) - i - 1]) * (16 ** i)
    return result


def binary_string_decode(binary):  # Converts from binary to decimal.
    binary = int(binary) if str(binary)[1] != 'b' else int(binary[2:])  # Condition for prefix.
    result = 0
    counter = 0
    while int(binary) > 0:  # Basic binary to decimal conversion.
        result += (int(binary) % 10) * (2 ** counter)
        binary //= 10
        counter += 1
    return result


def binary_to_hex(binary):  # Converts from binary to hexadecimal.
    binary = binary if binary[1] != 'b' else binary[2:]  # Condition for prefix.
    binary_list = []
    binary = ((4 - len(binary)) % 4) * "0" + binary
    # ^ Adds zeros to the front of the string, so it's length is a multiple of 4.
    for i in range(0, len(binary), 4):  # Fragments the string into a list of strings length 4.
        binary_list.append(binary[i:i + 4])
    result = ""
    for i in reversed(range(len(binary_list))):  # Using reversed() because binary_list is reversed.
        digit = binary_string_decode(int(binary_list[i]))  # Realizes every hex digit is 4 binary digits.
        if digit > 9:
            digit = chr((digit - 10) + ord('A'))  # Uses unicode to represent digits >9.
        result = str(digit) + result
    return result


if __name__ == '__main__':
    quit4 = False  # Stops the main loop.
    while not quit4:  # Calls functions for each menu selection.
        num, enter_option = menu(True)
        if enter_option == "1":
            print(f"Result: {hex_string_decode(num)}\n")
        if enter_option == "2":
            print(f"Result: {binary_string_decode(num)}\n")
        if enter_option == "3":
            print(f"Result: {binary_to_hex(num)}\n")
        if enter_option == "4":
            quit4 = True
            print("Goodbye!")