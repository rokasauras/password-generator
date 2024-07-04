import random  # Imports the random module for generating random choices
import string  # Imports the string module for easy access to character sets
import os      # Imports the os module to interact with the operating system

def random_password(length, use_punctuation=True):
    """Generates a random password of specified length."""
    # Create a base character set with letters and digits
    characters = string.ascii_letters + string.digits
    
    # Add punctuation to the character set if use_punctuation is True
    if use_punctuation:
        characters += string.punctuation
    
    # Generate the password by randomly selecting characters
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    # Prompt the user to enter the desired password length
    password_length = int(input("Enter the password length: "))
    
    # Ask the user if they want to include punctuation in the password
    include_punctuation = input("Include punctuation? (yes/no): ").strip().lower() == 'yes'
    
    # Generate the password
    password = random_password(password_length, include_punctuation)
    
    # Define the path to the desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    
    # Define the path to the password file
    file_path = os.path.join(desktop_path, 'password.txt')
    
    # Check if the file already exists
    if os.path.exists(file_path):
        print("File already exists. Please delete or rename the existing 'password.txt' file and try again.")
    else:
        # Write the password to the file
        with open(file_path, 'w') as file:
            file.write(password)
        
        print(f"Generated password: {password}")
        print(f"Password saved to: {file_path}")
