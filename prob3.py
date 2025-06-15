def multply(p1, p2):
    if isinstance(p1, str) and isinstance(p2, int):
        return p1 * p2
    elif isinstance(p1, int) and isinstance(p2, str):
        return p2 * p1
    elif isinstance(p1, (int, float)) and isinstance(p2, (int, float)):
        return p1 * p2
    else:
        raise TypeError("Unsupported types for multiplication")

def convert_input(value):
    try:
        # Try int
        return int(value)
    except ValueError:
        try:
            # Try float
            return float(value)
        except ValueError:
            # Return original string
            return value

num1 = convert_input(input('Enter first number: '))
num2 = convert_input(input('Enter second number: '))

try:
    print(f'The result of multiplying {num1} and {num2} is  {multply(num1, num2)}')
except TypeError as e:
    print("❌ Error:", e)
