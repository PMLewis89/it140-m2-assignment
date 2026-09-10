
"""Calculate and display a user's approximate birth year.

Input:
    User's name as a string entered from the keyboard.
    User's age as an integer entered from the keyboard.

Process:
    Subtract the user's age from the current year.

Output:
    A personalized message displaying the user's name and birth year.

Typical usage example:
    What is your name? Paris
    How old are you? 37
    Hello Paris! You were born in 1989.
"""

# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"\nHello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# OpenAI. (2026). ChatGPT [Large language model].
# Used for guidance with Python syntax, formatting, and assignment organization.
