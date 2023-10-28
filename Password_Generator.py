# Import modules
import sys
import os
import random
import string
import re

# Function to check the option you want at the beginning
def checking_program_option(program_choice):
    try:
        num = int(program_choice)
        if num in range(1,3):
            return True
        else:
            return False
    except ValueError:
        return False

# Function to validate the input password
def checking_password(input):
    # Custom special characters string
    special_characters = "!@#$%^&*()-_+=[]{}|;:'\"<>,.?/\\`~"

    return isinstance(input, str) and all(
        char.isalnum() or char.isspace() or not char.isprintable() or char in special_characters
        for char in input
    )

#Function to get the recommendations about the password
def get_recommendations(password):
    result = set()  # A set to store unique sentences

    # Custom special characters string
    special_characters = "!@#$%^&*()-_+=[]{}|;:'\"<>,.?/\\`~"

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        result.add("- Incorporate special characters into your password.")

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        result.add("- Ensure that your password includes uppercase letters.")

    # Check for spaces
    if ' ' in password:
        result.add("- Your password must not contains spaces.")

    # Check for special characters (non-alphanumeric)
    if not any(char in special_characters for char in password):
        result.add("- Incorporate special characters into your password.")

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        result.add("- Include numbers in your password.")

    return list(result)  # Convert the set back to a list

# Function to validate the number of passwords
def checking_num_of_passwords(number_of_passwords):
    try:
        num = int(number_of_passwords)
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
print("- Discover the power of password strength assessment and receive tailored recommendations.")
print("- Craft robust and secure passwords effortlessly with this program.")
print("- Let's customize your passwords together. Follow the prompts below.\n")
print("How can we assist you:")
print("1- Test your password strength.")
print("2- Customize a secure and strong password/passwords.")

# Input your choice
program_choice = input("Enter your choice: ")
validate_program_choice = checking_program_option(program_choice)

if validate_program_choice:
    os.system("cls")
    program_choice = int(program_choice)

    if (program_choice==1):
        # Input your password
        get_password = input("Please Enter your password: ")
        validate_password = checking_password(get_password)

        if validate_password:
            result = get_recommendations(get_password)

            # Checking the length of the password
            if (len(get_password)<8):
                result.append("- Maintain a minimum password length of at least 8 characters.")

            size = len(result)
            if (size==0):
                print("\nThe password you use is both reliable and strong.")
            elif (size==1):
                print("\nOur only recommendation is:")
                for recommendation in result:
                    print(recommendation)
            else:
                print("\nOur recommendations are:")
                # Iterate through the list of recommendations
                for recommendation in result:
                    print(recommendation)
            print("\nThanks for using our program.")
            input()
            sys.exit(0)
        else:
            os.system("cls")
            print("Please enter only a positive integer number.")
            input()
            sys.exit(1)
    else:
        # Input the number of required passwords
        number_of_passwords = input("Enter the number of required passwords: ")
        validate_num_of_passwords = checking_num_of_passwords(number_of_passwords)

        # Check if the number of passwords is valid
        if validate_num_of_passwords:
            os.system("cls")
            number_of_passwords = int(number_of_passwords)

            # Determine if singular or plural passwords
            if (number_of_passwords==1):
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
                if (number_of_passwords==1):
                    length = (input("Enter the length of your desired password: "))
                else:
                    length = (input("Enter the length of your desired passwords: "))
                validate_length = checking_length(length)

                # Check if the length is valid
                if validate_length:
                    os.system("cls")
                    length = int(length)

                    # Generate and display password based on user choices
                    if (number_of_passwords==1):
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
                                input()
                                sys.exit(1)

                    else:
                        # Generate and display passwords based on user choices
                        os.system("cls")

                        if (choice==1):
                            # Generate and display multiple passwords with capital letters
                            print("Your passwords are: ")
                            while number_of_passwords:
                                generated_password = "".join(random.choices(string.ascii_uppercase, k=length))
                                print(f"-  {generated_password}")
                                number_of_passwords -= 1
                        elif (choice==2):
                            # Generate and display multiple passwords with small letters
                            print("Your passwords are: ")
                            while number_of_passwords:
                                generated_password = "".join(random.choices(string.ascii_lowercase, k=length))
                                print(f"-  {generated_password}")
                                number_of_passwords -= 1
                        elif (choice==3):
                            # Generate and display multiple passwords with digits
                            print("Your passwords are: ")
                            while number_of_passwords:
                                generated_password = "".join(random.choices(string.digits, k=length))
                                print(f"-  {generated_password}")
                                number_of_passwords -= 1
                        elif (choice==4):
                            # Generate and display multiple passwords with special characters
                            print("Your passwords are: ")
                            special_characters = "@)${#(&*_>-~%<}"
                            while number_of_passwords:
                                generated_password = "".join(random.choice(special_characters) for _ in range(length))
                                print(f"-  {generated_password}")
                                number_of_passwords -= 1
                        elif (choice==5):
                            # Generate and display multiple passwords with all characters
                            print("Your passwords are: ")
                            special_characters = "@)${#(&*_>-~%<}"
                            all_characters = string.ascii_letters + string.digits + special_characters
                            while number_of_passwords:
                                generated_password = "".join(random.choice(all_characters) for _ in range(length))
                                print(f"-  {generated_password}")
                                number_of_passwords -= 1
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
                                while number_of_passwords:
                                    generated_password = "".join(random.choice(selected_options) for _ in range(length))
                                    print(f"-  {generated_password}")
                                    number_of_passwords -= 1
                            else:
                                # If the custom choice is invalid
                                os.system("cls")
                                print("Invalid options. Choose from the available options based on the selection criteria.")
                                input()
                                sys.exit(1)

                    # Exit the program after generating passwords
                    print("\nThanks for using our program.")
                    input()
                    sys.exit(0)

                else:
                    # If the length is invalid
                    os.system("cls")
                    print("Please enter only a positive integer number (8-50 characters) for a strong password length.")
                    input()
                    sys.exit(1)

            else:
                # If the choice is invalid
                os.system("cls")
                print("Invalid choice. Please try again.")
                input()
                sys.exit(1)

        else:
            # If the number of passwords is invalid
            os.system("cls")
            print("Please enter only a positive number.")
            input()
            sys.exit(1)
else:
    os.system("cls")
    print("Invalid option, Please enter only '1' or '2'.")
    input()
    sys.exit(1)