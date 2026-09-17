"""
Step 1 Exercise: Arithmetic Product and Conditional Logic

Problem Statement:
Write a Python function called `calculate_product_or_sum(num1, num2)` that takes
two integer numbers:
- If the product of the two numbers is less than or equal to 1000, return their product.
- Otherwise, return their sum.

Examples:
- Case 1: num1 = 20, num2 = 30 -> 20 * 30 = 600 (<= 1000) -> returns 600
- Case 2: num1 = 40, num2 = 30 -> 40 * 30 = 1200 (> 1000) -> returns 70 (40 + 30)

How to test your solution:
Run this file with Python:
    python exercise_01.py
"""


def calculate_product_or_sum(num1: int, num2: int) -> int:
    """
    Calculate the product of two integers if it is <= 1000,
    otherwise calculate their sum.
    """
    # TODO: Write your code here
    # 1. Multiply num1 and num2
    # 2. Check if product <= 1000 using an `if` condition
    # 3. Return product if true, else return (num1 + num2)
    pass


# --- Automated Tests / Verification ---
if __name__ == "__main__":
    print("Running tests for Step 1 Exercise...")

    # Case 1
    case1_result = calculate_product_or_sum(20, 30)
    print(f"Test 1 (20, 30): got {case1_result}")
    assert case1_result == 600, f"Expected 600, got {case1_result}"

    # Case 2
    case2_result = calculate_product_or_sum(40, 30)
    print(f"Test 2 (40, 30): got {case2_result}")
    assert case2_result == 70, f"Expected 70, got {case2_result}"

    # Additional edge cases
    assert calculate_product_or_sum(25, 40) == 1000, "Expected 1000 when product is exactly 1000"
    assert calculate_product_or_sum(25, 41) == 66, "Expected 66 when product is 1025"

    print("\n🎉 All tests passed! You've successfully completed Step 1.")
