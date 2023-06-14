import re

def validate_name(name):
    """
    Validates the user name.

    Args:
        name: The user name.

    Returns:
        True if the name is valid, False otherwise.
    """
    if not name:
        return False

    if len(name) > 20:
        return False
    
    if not re.match(r'[a-zA-Z]',name):
        return False

    return True

def validate_email(email):
    """
    Validates the user email.

    Args:
        email: The user email.

    Returns:
        True if the email is valid, False otherwise.
    """
    if not email:
        return False

    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$', email):
        return False

    return True

def validate_password(password):
    """
    Validates the user password.

    Args:
        password: The user password.

    Returns:
        True if the password is valid, False otherwise.
    """
    if not password:
        return False

    if len(password) < 8:
        return False

    if not re.search(r'[0-9]', password):
        return False

    if not re.search(r'[a-zA-Z]', password):
        return False

    return True

def validate_phone(phone_number):
    if(len(phone_number)>10):
      return False
    
    if not re.match(r"^[0-9]{10}$",phone_number):
      return False
    
    return True

def main():
    """
    The main function.
    """
    name = input("Enter your name: ")
    if not validate_name(name):
        print("Invalid name.")
        return
    
    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email.")
        return
    
    phone_number = input("Enter your phone number: ")
    if not validate_phone(phone_number):
        print("Invalid Phone Number.")
        return
    
    password = input("Enter your password(Minimum, 8 char, 1 caps, 1 digit): ")
    if not validate_password(password):
        print("Invalid password.")
        return
    

    print("Your form has been submitted successfully.")


if __name__ == "__main__":
    main()
