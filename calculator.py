"""
Smart Calculator - Simple CLI Calculator
Demonstrating Git workflows and version control concepts.
"""

import sys


def calculate(a, b, operation="add"):
    """
    Perform calculation on two numbers.
    Supports both addition and multiplication operations.
    """
    if operation in ("add", "+"):
        return a + b  # Addition feature
    elif operation in ("multiply", "*"):
        return a * b  # Multiplication feature
    else:
        raise ValueError(f"Unsupported operation: {operation}")


def main():
    print("=" * 40)
    print("       SMART CALCULATOR (v1.0)")
    print("=" * 40)

    try:
        val1 = input("Enter first number: ").strip()
        a = float(val1)

        val2 = input("Enter second number: ").strip()
        b = float(val2)

        op = input("Choose operation (+ or * / add or multiply) [default: +]: ").strip().lower()
        if not op:
            op = "add"
    except ValueError:
        print("\n[Error] Invalid input. Please enter valid numeric values.")
        sys.exit(1)

    try:
        result = calculate(a, b, op)
        print("-" * 40)
        print(f"Result: {result}")
        print("=" * 40)
    except ValueError as err:
        print(f"\n[Error] {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()