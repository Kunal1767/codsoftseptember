import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the password length: "))
        
        if length <= 0:
            print("Invalid input. Password length must be a positive integer.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
