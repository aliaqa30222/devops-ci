import sys

def decimal_to_hex(decimal_value):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""

    try:
        num = int(decimal_value)  # Ensure input is an integer
        if num < 0:
            raise ValueError("Negative numbers are not supported.")

        print(f"Converting the Decimal Value {num} to Hex...")

        if num == 0:
            return "0"

        while num > 0:
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16

        print(f"Hexadecimal representation is: {hexadecimal}")
        return hexadecimal

    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input provided. Please enter a decimal number.")
        sys.exit(1)

    decimal_to_hex(sys.argv[1])

