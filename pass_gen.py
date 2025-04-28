import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all = lower + upper + numbers + symbols
length = 10

def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = "".join(random.sample(all, length))
    return password

password = generate_password(length)
if password:
    print(password)

