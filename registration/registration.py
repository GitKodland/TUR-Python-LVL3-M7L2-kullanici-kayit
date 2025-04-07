# user_management.py

def initialize_users():
    """Returns a predefined dictionary of users."""
    return {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3",
        "user4": "password4",
        "user5": "password5",
    }

def add_user(users, username, password):
    """Adds a new user if they are not already in the dictionary.
    Returns the updated dictionary of users."""
    # Task: if the user already exists, return the message - "A user with this login already exists."
    # Task: if the user is not in the dictionary, add a new entry to the dictionary, where the key is the username and the value is the password.
    return f"New user {username} has been added successfully."

def display_users(users):
    """Displays a list of all users and their passwords."""
    print("The following users with their passwords are already registered in the system:")
    for username, password in users.items():
        print(f"Login: {username}, Password: {password}")

def main():
    users = initialize_users()
    display_users(users)

    print("\nYou can add a new user.")
    username = input("Enter the login of the new user: ")
    password = input("Enter the password of the new user: ")
    result = add_user(users, username, password)
    print(result)

    print("\nList of all users after adding a new one:")
    display_users(users)

if __name__ == "__main__":
    main()