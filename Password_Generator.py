# Import modules
import sys
import os
import random
import string
import re

# Function to validate the number of passwords
def checking_num_of_passwords(num_words):
    try:
        num = int(num_words)
        if (num>0):
            return True
        else:
            return False
    except ValueError:
        return False

# Function to validate the choice of password components
def checking_choice(choice):
    try:
        num = int(choice)
        if num in range(1,7):
            return True
        else:
            return False
    except ValueError:
        return False

# Function to validate the password length
def checking_length(length):
    try:
        num = int(length)
        if num in range(8,51):
            return True
        else:
            return False
    except ValueError:
        return False

# Function to validate custom choice format
def checking_options(custom_choice):
    pattern = r"^(?!.*1.*2.*3.*4)[1-4](,[1-4]){1,2}$"
    if re.match(pattern, custom_choice):
        return True
    else:
        return False

# Main program starts here

# Print welcome message and instructions
print("Welcome to the Password Generator!")
print("- Craft robust and secure passwords effortlessly with this program.")
print("- Let's customize your passwords together. Follow the prompts below.\n")

# Input the number of required passwords
num_words = input("Enter the number of required passwords: ")
validate_num_of_passwords = checking_num_of_passwords(num_words)

# Check if the number of passwords is valid
if validate_num_of_passwords:
    os.system("cls")
    num_words = int(num_words)

    # Determine if singular or plural passwords
    if (num_words==1):
        print("Choose the components for your password: ")
    else:
        print("Choose the components for your passwords: ")

    # Display available password component options
    print("1- Capital English Letters.")
    print("2- Small English Letters.")
    print("3- Numbers.")
    print("4- Special Characters.")
    print("5- Include All Of The Above.")
    print("6- Custom Choice.")

    # Input the choice of password components
    choice = input("Enter your choice: ")
    validate_choice = checking_choice(choice)

    # Check if the choice is valid
    if validate_choice:
        os.system("cls")
        choice = int(choice)

        # Input the desired password length
        if (num_words==1):
            length = (input("Enter the length of your desired password: "))
        else:
            length = (input("Enter the length of your desired passwords: "))
        validate_length = checking_length(length)

        # Check if the length is valid
        if validate_length:
            os.system("cls")
            length = int(length)

            # Generate and display password based on user choices
            if (num_words==1):
                # Clear the screen
                os.system("cls")

                if (choice==1):
                    # Generate and display password with capital letters
                    print("Your password is: ", end="")
                    generated_password = "".join(random.choices(string.ascii_uppercase, k=length))
                    print(generated_password)
                elif (choice==2):
                    # Generate and display password with small letters
                    print("Your password is: ", end="")
                    generated_password = "".join(random.choices(string.ascii_lowercase, k=length))
                    print(generated_password)
                elif (choice==3):
                    # Generate and display password with digits
                    print("Your password is: ", end="")
                    generated_password = "".join(random.choices(string.digits, k=length))
                    print(generated_password)
                elif (choice==4):
                    # Generate and display password with special characters
                    print("Your password is: ", end="")
                    special_characters = "@)${#(&*_>-~%<}"
                    generated_password = "".join(random.choice(special_characters) for _ in range(length))
                    print(generated_password)
                elif (choice==5):
                    # Generate and display password with all characters
                    print("Your password is: ", end="")
                    special_characters = "@)${#(&*_>-~%<}"
                    all_characters = string.ascii_letters + string.digits + special_characters
                    generated_password = "".join(random.choice(all_characters) for _ in range(length))
                    print(generated_password)
                else: # (choice==6)
                    # Handle custom choice input
                    os.system("cls")

                    # Display available custom choice password options
                    print("Enter numbers (1-4) separated by commas for desired password options.")
                    print("You can select either two or three choices only, (for example: 1,3,4 or 2,1).")
                    print("1- Capital English Letters.")
                    print("2- Small English Letters.")
                    print("3- Numbers.")
                    print("4- Special Characters.")

                    # Input the custom choice
                    custom_choice = input("Enter the numbers of your chosen options: ")
                    validate_custom_choice = checking_options(custom_choice)
                    os.system("cls")

                    # Check if the custom choice is valid
                    if validate_custom_choice:

                        # Split the custom choice into a list of integers
                        choices_list = custom_choice.split(',')
                        choices_list = [int(num) for num in choices_list]

                        # Define a string of special characters
                        special_characters = "@)${#(&*_>-~%<}"

                        # Initialize an empty string to store the selected options
                        selected_options = ""

                        # Iterate through the list of choices
                        for num in choices_list:
                            if (num==1):
                                # Include capital English letters
                                selected_options += string.ascii_uppercase
                            elif (num==2):
                                # Include small English letters
                                selected_options += string.ascii_lowercase
                            elif (num==3):
                                # Include numbers
                                selected_options += string.digits
                            else: # (num==4)
                                # Include special characters
                                selected_options += special_characters

                        # Generate and display password with the selected options
                        print("Your password is: ", end="")
                        generated_password = "".join(random.choice(selected_options) for _ in range(length))
                        print(generated_password)
                    else:
                        # If the custom choice is invalid
                        os.system("cls")
                        print("Invalid options. Choose from the available options based on the selection criteria.")
                        sys.exit(0)

            else:
                # Generate and display passwords based on user choices
                os.system("cls")

                if (choice==1):
                    # Generate and display multiple passwords with capital letters
                    print("Your passwords are: ")
                    while num_words:
                        generated_password = "".join(random.choices(string.ascii_uppercase, k=length))
                        print(f"-  {generated_password}")
                        num_words -= 1
                elif (choice==2):
                    # Generate and display multiple passwords with small letters
                    print("Your passwords are: ")
                    while num_words:
                        generated_password = "".join(random.choices(string.ascii_lowercase, k=length))
                        print(f"-  {generated_password}")
                        num_words -= 1
                elif (choice==3):
                    # Generate and display multiple passwords with digits
                    print("Your passwords are: ")
                    while num_words:
                        generated_password = "".join(random.choices(string.digits, k=length))
                        print(f"-  {generated_password}")
                        num_words -= 1
                elif (choice==4):
                    # Generate and display multiple passwords with special characters
                    print("Your passwords are: ")
                    special_characters = "@)${#(&*_>-~%<}"
                    while num_words:
                        generated_password = "".join(random.choice(special_characters) for _ in range(length))
                        print(f"-  {generated_password}")
                        num_words -= 1
                elif (choice==5):
                    # Generate and display multiple passwords with all characters
                    print("Your passwords are: ")
                    special_characters = "@)${#(&*_>-~%<}"
                    all_characters = string.ascii_letters + string.digits + special_characters
                    while num_words:
                        generated_password = "".join(random.choice(all_characters) for _ in range(length))
                        print(f"-  {generated_password}")
                        num_words -= 1
                else: # (choice==6)
                    # Handle custom choice input for multiple passwords

                    # Display available custom choice passwords options
                    print("Enter numbers (1-4) separated by commas for desired passwords options.")
                    print("You can select either two or three choices only, (for example: 1,3,4 or 2,1).")
                    print("1- Capital English Letters.")
                    print("2- Small English Letters.")
                    print("3- Numbers.")
                    print("4- Special Characters.")

                    # Input the the custom choice
                    custom_choice = input("Enter the numbers of your chosen options: ")
                    validate_custom_choice = checking_options(custom_choice)
                    os.system("cls")

                    # Check if the custom choice is valid
                    if validate_custom_choice:

                        # Split the custom choice into a list of integers
                        choices_list = custom_choice.split(',')
                        choices_list = [int(num) for num in choices_list]

                        # Define a string of special characters
                        special_characters = "@)${#(&*_>-~%<}"

                        # Initialize an empty string to store the selected options
                        selected_options = ""

                        # Iterate through the list of choices
                        for num in choices_list:
                            if (num==1):
                                # Include capital English letters
                                selected_options += string.ascii_uppercase
                            elif (num==2):
                                # Include small English letters
                                selected_options += string.ascii_lowercase
                            elif (num==3):
                                # Include numbers
                                selected_options += string.digits
                            else: # (num==4)
                                # Include special characters
                                selected_options += special_characters

                        # Generate and display passwords with the selected options
                        print("Your passwords are: ")
                        while num_words:
                            generated_password = "".join(random.choice(selected_options) for _ in range(length))
                            print(f"-  {generated_password}")
                            num_words -= 1
                    else:
                        # If the custom choice is invalid
                        os.system("cls")
                        print("Invalid options. Choose from the available options based on the selection criteria.")
                        sys.exit(0)

            # Exit the program after generating passwords
            print("Thanks for using our program.")
            sys.exit(0)

        else:
            # If the length is invalid
            os.system("cls")
            print("Please enter only a positive integer number (8-50 characters) for a strong password length.")
            sys.exit(0)

    else:
        # If the choice is invalid
        os.system("cls")
        print("Invalid choice. Please try again.")
        sys.exit(0)

else:
    # If the number of passwords is invalid
    os.system("cls")
    print("Please enter only a positive number.")
    sys.exit(0)