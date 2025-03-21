
#Updated file

import sys

def decimal_to_hex(decimal_value):
    # Validate input
    if decimal_value is None:
        raise ValueError("Input cannot be None")
    if not isinstance(decimal_value, int):
        raise ValueError("Input must be an integer")

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    # Handle the edge case for 0
    if num == 0:
        print("Hexadecimal representation is: 0")
        return "0"

    print(f"Converting the Decimal Value {num} to Hex...")
    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError:
            print("Please provide a valid integer.")
    else:
        print("Usage: python script.py <decimal_number>")


