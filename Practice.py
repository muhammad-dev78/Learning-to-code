"""
File: practice.py
Author: Muhammad Hussein
Purpose: Full Stack Development Practice (Beginner → Pro)
Created: 23 December 2025
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


# =============================
# CONDITIONALS PRACTICE 
# =============================
def check_developer_level(years_of_experience):
         print("DEVELOPER LEVEL")
         
         if years_of_experience < 1:
              print("Beginner")
         elif years_of_experience < 3:
             print("junior")
         elif years_of_experience < 5:
             print("Mid Level")
         else:
                print("Senior")

# =============================
# MAIN PROGRAM
# =============================
def main():
    check_developer_level(0)

if __name__ == "__main__":
    main()


#  =============================
#  LOGICAL OPERATORS PRACTICE
#  =============================
def check_access(age, has_id):
    """Practice logical operators: and, or, not"""
    print("ACCESS CHECK")
    if age >= 18 and has_id:
      print("Access Granted")
    elif age >= 18 and not has_id:
        print("ID Required")
    elif age < 18 or not has_id:
        print("Access Denied")

#  =============================
#  MAIN PROGRAM
#  =============================
def main():
    check_access(21, True)
    check_access(20, False)
    check_access(30, True)

if __name__ == "__main__":
    main()


#  =============================
#  ACCESS CHECK WITH INPUT
#  =============================
def    check_access(age, has_id):
    print("\nACCESS CHECK")
    
    if age >= 18 and has_id:
        print("Access Granted")
    elif age >= 18 and not has_id:
       print("ID Required")
    else:
       print("Access Denied")

#  - - - User input - - -
# =============================
# MAIN PROGRAM
# =============================

def main():
    age = int(input( "Enter your age: "))
    id_input = input( "Do you have an ID? (yes/no): ")

has_id = id_input.lower() == "yes"
check_access(age, has_id)

if __name__ == "__main__":
    main()
