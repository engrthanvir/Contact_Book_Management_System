def validate_name(name):
    if not isinstance(name, str) or not name.strip() or name.isdigit():
        raise ValueError("Name must be a non-empty string and not just a number.!!! Please enter name correctly.")
    return name

def validate_phone(phone):
    if not phone.isdigit():
        raise ValueError("Phone number must be numeric! Please enter a number.")
    
    if len(phone) > 11:
        raise ValueError("Phone number cannot be more than 11 digits.")
    
    return phone


def validate_email(email):
    if not isinstance(email, str):
        raise ValueError("Email must be a string.")
    

    if email.count('@') != 1:
        raise ValueError("Email must contain exactly one '@' symbol.")
    

    local_part, domain_part = email.split('@')
    

    if not local_part or not domain_part:
        raise ValueError("Email local part and domain part must not be empty.")
    

    if '.' not in domain_part:
        raise ValueError("Domain part of the email must contain a '.' symbol.")
    

    if domain_part not in ['gmail.com', 'yahoo.com']:
        raise ValueError("Email must be from either gmail.com or yahoo.com.")
    
    return email

def validate_address(address):
    if not isinstance(address, str):
        raise ValueError("Address must be a string.")
    
    address = address.strip()
    
    if not address:
        raise ValueError("Address cannot be empty.")
    
    return address