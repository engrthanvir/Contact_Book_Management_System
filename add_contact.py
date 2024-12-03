from utils import validate_name, validate_phone, validate_email,validate_address  # Assuming validate_email is imported

def add_contact(contact_book):
    while True:
        try:
            name = validate_name(input("Enter name: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    while True:
        try:
            email = input("Enter email: ")
            validate_email(email)
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    while True:
        try:
            phone = validate_phone(input("Enter phone number: "))
            break
        except ValueError as e:
            print(f"Error: {e}")
    
    while True:
        try:
            address = input("Enter address: ")
            validate_address(address)
            break
        except ValueError as e:
            print(f"Error: {e}")
    

    print(contact_book.add_contact(name, email, phone, address))
    return True
