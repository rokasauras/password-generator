# Password Generator

## Description

This Python script generates a secure password with a specified length. The generated password includes a combination of lowercase letters, uppercase letters, and digits in a random order.

## How to Use

1. **Save the Python File:**
   - Download and save the `password_generator.py` file on your computer.

2. **Run the Script:**
   - Open your terminal or command prompt.
   - Navigate to the directory where `password_generator.py` is saved.
   - Run the script using Python:
     ```
     python password_generator.py
     ```

3. **Enter Password Length:**
   - You will be prompted to enter the desired password length.
   - Input a number and press **Enter**.

4. **Generated Password:**
   - The script will generate a password of the specified length and display it on the terminal.

## To Improve

1. **Include Support for Symbols:**
   - Modify the script to include symbols (such as `!@#$%^&*()`) in the generated passwords for added complexity.

2. **Include Support for Saving Credentials:**
   - Enhance the script to save generated passwords securely to a file, possibly encrypted or in a format that protects sensitive information.

3. **Implement GUI (Graphical User Interface):**
   - Develop a graphical interface using a library like Tkinter or PyQt to make the password generation process more user-friendly.

4. **Add arrows or sliders to GUI

## Example

```python
import random
import string

def random_password(password_length):
    # Generates a random password including lowercase, uppercase letters, and digits
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the password length: "))
    generated_password = random_password(password_length)
    print(f"Generated Password: {generated_password}")
