# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result or a message if division by zero."""
    if b == 0:
        print("Cannot divide by 0")
        return None
    return a / b

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

if __name__ == "__main__":
    x = 10
    y = 0

    # Call divide_numbers
    result = divide_numbers(x, y)
    if result is not None:
        print(f"The result of division is: {result}")

    # Call multiply_numbers
    product = multiply_numbers(x, y)
    print(f"The result of multiplication is: {product}")
