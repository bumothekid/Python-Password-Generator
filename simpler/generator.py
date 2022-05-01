import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"

while True:
    password_len = int(input("What length would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))
    for _ in range(password_count):
        password  = ""
        for _ in range(password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Here is your password : ", password)
    exit(0)
