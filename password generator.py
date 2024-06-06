import numpy
import random
import string

password_length = int(input("Enter the password length : "))

def random_password(password_length):
     inp_list = [(random.choice(string.ascii_letters+string.digits)) for i in range(password_length)]
     out_str = ""
     return(out_str.join(inp_list))

print(random_password(password_length))






