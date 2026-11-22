"""
Smart Calculator - Simple CLI Calculator
Demonstrating Git workflows and version control concepts.
"""

import sys


def calculate(a, b):
    """
    Perform calculation on two numbers.
    Initially supports basic addition.
    """
    return a + b  # Addition feature


def main():
    print("=" * 40)
    print("       SMART CALCULATOR (v1.0)")
    print("=" * 40)

    try:
        val1 = input("Enter first number: ").strip()
        a = float(val1)

        val2 = input("Enter second number: ").strip()
        b = float(val2)
    except ValueError:
        print("\n[Error] Invalid input. Please enter valid numeric values.")
        sys.exit(1)

    result = calculate(a, b)
    print("-" * 40)
    print(f"Result: {result}")
    print("=" * 40)


if __name__ == "__main__":
    main()

