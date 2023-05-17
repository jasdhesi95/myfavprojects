import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Welcome to the Password Generator!")
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
