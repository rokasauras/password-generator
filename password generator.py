import random  # Imports the random module for generating random choices
import string  # Imports the string module for easy access to character sets

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
    
    # Print the generated password
    print("Generated password:", random_password(password_length, include_punctuation))
