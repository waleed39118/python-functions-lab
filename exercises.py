# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()




# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():

    letter = input("Enter a single letter (a-z or A-Z): ").strip()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single alphabetical letter.")
        return

    # Converting to lowercase for uniform comparison
    lower_letter = letter.lower()

    # Defining vowels
    vowels = 'aeiou'

    # Checking if the letter is a vowel or consonant
    if lower_letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")    # Your control flow logic goes here

check_letter()



# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    try:
        age_input = input("Please enter your age: ").strip()
        age = int(age_input)

        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return

        # Seting the minimum voting age
        voting_age = 18

        # Checking eligibility
        if age >= voting_age:
            print(f"You are {age} years old. You are eligible to vote.")
        else:
            print(f"You are {age} years old. You are not eligible to vote yet.")

        print("Invalid input. Please enter a numeric value for age.")

# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():

        age_input = input("Input a dog's age: ").strip()
        dog_age = int(age_input)

        # Validating that the age is non-negative
        if dog_age < 0:
            print("Age cannot be negative. Please enter a valid age.")
            return

        # Calculating dog years
        if dog_age == 0:
            dog_years = 0
        elif dog_age == 1:
            dog_years = 10
        elif dog_age == 2:
            dog_years = 20
        else:
            dog_years = 20 + (dog_age - 2) * 7

        print(f"The dog's age in dog years is {dog_years}.")

    excepting ValueError:
        print("Invalid input. Please enter a numeric value for the dog's age.")

# Call the function
calculate_dog_years()



# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():

    cold_input = input("Is it cold? (yes/no): ").strip().lower()
    rain_input = input("Is it raining? (yes/no): ").strip().lower()

    # Validating inputs
    valid_responses = ['yes', 'no']
    if cold_input not in valid_responses or rain_input not in valid_responses:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return

    # Converting responses to boolean values
    is_cold = cold_input == 'yes'
    is_raining = rain_input == 'yes'

    # Determining clothing advice
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()



# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():

    months_31 = ['Jan', 'Mar', 'May', 'Jul', 'Aug', 'Oct', 'Dec']
    months_30 = ['Apr', 'Jun', 'Sep', 'Nov']
    feb = 'Feb'
    all_months = months_31 + months_30 + [feb]

    # Prompting for month
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()

    # Validating month
    if month not in all_months:
        print("Invalid month. Please enter a valid three-letter month abbreviation (e.g., Jan, Feb).")
        return

    # Prompting for day
        day = int(input("Enter the day of the month: ").strip())
    except ValueError:
        print("Invalid day. Please enter a numeric value.")
        return

    # Validating day range
    if month in months_31 and not (1 <= day <= 31):
        print(f"{month} has 31 days. Please enter a valid day.")
        return
    elif month in months_30 and not (1 <= day <= 30):
        print(f"{month} has 30 days. Please enter a valid day.")
        return
    elif month == feb and not (1 <= day <= 29):  # Accepting up to 29 for leap years
        print("February has 28 or 29 days. Please enter a valid day.")
        return

    # Determining season
    if (month == 'Dec' and day >= 21) or month in ['Jan', 'Feb'] or (month == 'Mar' and day <= 19):
        season = 'Winter'
    elif (month == 'Mar' and day >= 20) or month in ['Apr', 'May'] or (month == 'Jun' and day <= 20):
        season = 'Spring'
    elif (month == 'Jun' and day >= 21) or month in ['Jul', 'Aug'] or (month == 'Sep' and day <= 21):
        season = 'Summer'
    elif (month == 'Sep' and day >= 22) or month in ['Oct', 'Nov'] or (month == 'Dec' and day <= 20):
        season = 'Fall'
    else:
        season = 'Unknown'  # Fallback, shouldn't happen with valid input

    print(f"{month} {day} is in {season}.")

# Call the function
determine_season()



# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    target = 42  # Fixed number to guess
    max_attempts = 5

    print("Guess the number between 1 and 100. You have 5 attempts!")

    for attempt in range(1, max_attempts + 1):
            guess = int(input(f"Attempt {attempt}: Enter your guess: ").strip())

            # Validating range
            if guess < 1 or guess > 100:
                print("Your guess must be between 1 and 100.")
                continue

            # Checking guess
            if guess == target:
                print("Congratulations, you guessed correctly!")
                return
            elif guess < target and guess != target:
                print("Guess is too low.")
            elif guess > target and guess != target:
                print("Guess is too high.")

            # Final attempt warning
            if attempt == max_attempts:
                print("Last chance!" if guess != target else "")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Sorry, you failed to guess the number in five attempts.")

# Call the function
guess_number()


