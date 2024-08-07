# Password Generator

## Description

This Python script generates a secure password with a specified length. The generated password includes a combination of lowercase letters, uppercase letters, and digits in a random order. It now asks whether you'd like to 
include special characters in your generated password.

## How to Use

1. **Save the Python File:**
   - Download and save the `password_generator.py` file on your computer.

2. **Run the Script:**
   - Open your terminal.
   - Navigate to the directory where `password_generator.py` is saved.
   - Run the script using Python:
     ```
     python password_generator.py
     ```

3. **Enter Password Length:**
   - You will be prompted to enter the desired password length.
   - Input a number and press **Enter**.

4. **Include special characters?**
   -You will be promted to enter yes/no to special characters
   -Input yes/no


5. **Generated Password:**
   - The script will generate a password of the specified length and display it on the terminal.

## To Improve

1. **Include Support for Saving Credentials:**
   - Enhance the script to save generated passwords securely to a file, possibly encrypted or in a format that protects sensitive information.

2. **Implement GUI (Graphical User Interface):**
   - Develop a graphical interface using a library like Tkinter or PyQt to make the password generation process more user-friendly.

3. **Add arrows or sliders to GUI**

## Example

```python
$ python password_generator.py
Enter the password length: 12
Include punctuation? (yes/no): yes
Generated password: aB1$cDeFgH!2
