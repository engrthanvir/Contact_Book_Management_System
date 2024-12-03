class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone_number, address):

        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                return "Error: Phone number already exists!"
        

        new_contact = {
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address
        }
        self.contacts.append(new_contact)
        return f"Contact for {name} added successfully."

    def remove_contact(self, phone_number):

        for contact in self.contacts:
            if contact["phone_number"] == phone_number:
                self.contacts.remove(contact)
                return "Contact removed successfully."
        return "Error: Contact not found!"

    def view_contacts(self):

        if not self.contacts:
            return "No contacts available."
        contact_list = "\n".join(
            [f"{contact['name']} | {contact['email']} | {contact['phone_number']} | {contact['address']}" 
             for contact in self.contacts]
        )
        return contact_list

    def search_contacts(self, query):

        results = []
        for contact in self.contacts:
            if query.lower() in contact["name"].lower() or query.lower() in contact["email"].lower():
                results.append(f"{contact['name']} | {contact['email']} | {contact['phone_number']} | {contact['address']}")
        return "\n".join(results) if results else "No matches found."