import random
import time

def generatePassword():
    validCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"
    password = ""

    for i, _ in enumerate(range(20)):
        if i in [7, 14]: password += "-"; continue
        password += random.choice(validCharacters)
    
    if password == "":
        return "An error occured!"
    
    return password


if __name__ == "__main__":
    try:
        amount = int(input("How many passwords would you like to generate:\n"))
    except ValueError:
        print("Amount needs to be an integer")
        exit()

    if amount < 1:
        print("Amount needs to be greater than 0")
        exit()

    if amount > 100000:
        print("You can't generate more than 100000 passwords at once")
        print("I don't really understand why u would need that much passwords but you can't")
        exit()

    if amount > 100:
        sure = input(f"Are you sure you want to generate {amount} passwords? (y/n)\n")

        if sure not in ["y", "n", "yes", "no"]:
            print("Your anwser needs to be y or n")
            exit()

        if sure in ["n", "no"]:
            print("Exiting process")
            exit()
        
        print("Be aware that this might take a while go generate all passwords!")
        time.sleep(5)

    text = "Your password:"
    if amount > 1:
        print("Your passwords:")

    for _ in range(amount):
        print(generatePassword())
