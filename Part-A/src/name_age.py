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
2. Line 36 — calculate birth year

Delete:

birth_year = CURRENT_YEAR - age

Replace it with:

birth_year = CURRENT_YEAR - age
3. Line 39 — display the answer

Delete:

print(f"\nHello {name}! You were born in {birth_year}.")

Replace it with:

print(f"\nHello {name}! You were born in {birth_year}.")

So that whole part should look exactly like this:

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

Keep lines 42–44 exactly as they are.

Also keep this at the top:

from datetime import date

and:

CURRENT_YEAR = date.today().year

That's important because it satisfies the requirement not to hardcode 2025 or 2026.

Don't click Commit changes yet. After you enter those four lines, scroll back to the top of the file. We still need to complete the TODO documentation at the top before saving..

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.

    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# === References ===
# OpenAI. (2026). ChatGPT [Large language model].
# Used for guidance with Python syntax, formatting, and assignment organization.
