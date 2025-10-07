
# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    """Return the area of a triangle given base and height."""
    return (base * height) / 2

print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    rate is expected as a percentage (e.g., 5 for 5%).
    """
    return (principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
def apply_discount(price, discount_percent):
    """
    Apply discount_percent (0-100) to price and return the discounted price.
    If discount_percent is outside 0-100, it will still compute, but typical usage is 0..100.
    """
    return price * (1 - (discount_percent / 100))

print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature
def convert_temperature(value, unit):
    """
    Convert temperature.
    unit should be 'C' or 'F' (case-insensitive).
    Returns a float.
    """
    if unit in ('C', 'c'):
     
        return (value * 9 / 5) + 32
    elif unit in ('F', 'f'):
        
        return (value - 32) * 5 / 9
    else:
        
        return None

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
def sum_to(n):
    """
    Return the sum of integers from 1 to n.
    If n < 1, returns 0.
    """
    if n < 1:
        return 0
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))


# Exercise 6: Find the Largest Number
def largest(a, b, c):
    """Return the largest of three integers."""
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))


# Exercise 7: Calculate a Tip
def calculate_tip(bill_amount, tip_percent):
    """
    Calculate the tip amount.
    tip_percent is given as whole number (e.g., 20 for 20%).
    """
    return bill_amount * (tip_percent / 100)

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers
def product(*args):
    """
    Multiply all supplied numbers together and return the product.
    If no arguments are given, return 1 (multiplicative identity).
    """
    if len(args) == 0:
        return 1
    result = 1
    for n in args:
        result *= n
    return result

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic Calculator
def basic_calculator(a, b, operation):
    """
    Perform basic arithmetic.
    operation must be 'add', 'subtract', 'multiply', or 'divide' (case-insensitive).
    For divide, returns None on division by zero.
    """
    op = operation.lower()
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b == 0:
            return None
        return a / b
    else:
        return None  

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
