import re

def validate_email(email):
    # Improved regex for email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if len(email) > 7 and re.match(pattern, email):
        return True
    return False

if __name__ == "__main__":
    emails = input("Enter email addresses separated by commas: ")
    email_list = [e.strip() for e in emails.split(",")]
    for email in email_list:
        if validate_email(email):
            print(f"{email}: Valid")
        else:
            print(f"{email}: Invalid")

