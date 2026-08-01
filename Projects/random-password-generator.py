import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

all_characters = letters + numbers + symbols

password_length = int(input("Enter the desired password length: "))
password = ''.join(random.choice(all_characters) for _ in range(password_length))
print("Generated password:", password)