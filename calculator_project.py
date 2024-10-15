def add(a,b):
    """Add two numbers and return the result"""
    return a + b

def subtract(a,b):
    """Subtract b from a and return the result"""
    return a - b




print (f"5 + 3 =  {add(5,3)}")
print (f"10 - 4 = {subtract(10,4)}")

def multiply (a,b):
    return a*b
print (f"4 * 6 = {multiply4,6}")
def divide(a, b):
    """Divide a by b and return the result. Returns error message if b is zero."""
    return a / b if b != 0 else "Error: Division by zero"

# Test the new function
print(f"10 / 2 = {divide(10, 2)}")
print(f"5 / 0 = {divide(5, 0)}")
