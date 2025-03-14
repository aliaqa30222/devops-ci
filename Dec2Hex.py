import sys

def decimal_to_hex(decimal_value):
    if not isinstance(decimal_value, int):
        raise ValueError("Input must be an integer.")

    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    if not hexadecimal:
        hexadecimal = "0"

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":
    try:
        if len(sys.argv) <= 1:
            raise ValueError("No input provided. Usage: python script.py <decimal_number>")

        decimal_value = int(sys.argv[1])
        decimal_to_hex(decimal_value)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

