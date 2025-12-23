"""
File: practice.py
Author: Muhammad Hussein
Purpose: Full Stack Development Practice (Beginner → Pro)
Last Updated: 23 December 2025
"""

# =============================
# IMPORTS
# =============================
from utils.math_tools import add, subtract


# =============================
# USER PROFILE
# =============================
USER_PROFILE = {
    "name": "Muhammad",
    "age": 21,
    "location": "MSA",
    "goal": "Become a Full Stack Developer"
}


# =============================
# DISPLAY FUNCTIONS
# =============================
def display_user_profile(profile: dict) -> None:
    """Display user personal information"""
    print("=== USER PROFILE ===")
    print(f"Name     : {profile['name']}")
    print(f"Age      : {profile['age']}")
    print(f"Location : {profile['location']}")
    print(f"Goal     : {profile['goal']}")
    print("InshaAllah, success is guaranteed 💪\n")


# =============================
# BASIC PYTHON PRACTICE
# =============================
def basic_math_operations() -> None:
    """Practice basic Python math operations"""
    print("=== BASIC MATH OPERATIONS ===")
    print("Addition        :", 12 + 4)
    print("Subtraction     :", 12 - 10)
    print("Multiplication  :", 20 * 5)
    print("Division        :", 12 / 4)
    print("Floor Division  :", 50 // 10)
    print("Modulus         :", 50 % 10)
    print("Exponent        :", 4 ** 3)
    print()


# =============================
# MODULE PRACTICE
# =============================
def module_math_operations() -> None:
    """Using custom math_tools module"""
    print("=== MODULE MATH OPERATIONS ===")
    print("Add (module)      :", add(10, 5))
    print("Subtract (module) :", subtract(10, 5))
    print()


# =============================
# MAIN PROGRAM
# =============================
def main() -> None:
    display_user_profile(USER_PROFILE)
    basic_math_operations()
    module_math_operations()


if __name__ == "__main__":
    main()
