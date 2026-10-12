"""
Calculator Module implementing arithmetic operations.
Used for Gitflow workflow demonstration and automated CI/CD testing.
"""

def add(a: float, b: float) -> float:
    """Return sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return division result, raises ValueError on zero divisor."""
    if b == 0:
        raise ValueError("Division by zero is undefined.")
    return a / b

if __name__ == "__main__":
    print("Addition 10 + 5:", add(10, 5))
    print("Subtraction 10 - 5:", subtract(10, 5))
    print("Multiplication 10 * 5:", multiply(10, 5))
    print("Division 10 / 5:", divide(10, 5))
