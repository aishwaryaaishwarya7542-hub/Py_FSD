# Simple login system

USERNAME = "admin"
PASSWORD = "1234"
MAX_ATTEMPTS = 3


def login():
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"Attempt {attempt} of {MAX_ATTEMPTS}")
        entered_username = input("Enter username: ").strip()
        entered_password = input("Enter password: ").strip()

        if entered_username == USERNAME and entered_password == PASSWORD:
            print("Login successful!")
            return True

        remaining = MAX_ATTEMPTS - attempt
        if remaining > 0:
            print(f"Invalid username or password. {remaining} attempt(s) remaining.")
        else:
            print("Too many failed attempts. Access denied.")

    return False


if __name__ == "__main__":
    login()
