import csv
import os


CONTACTS_FOLDER = "contact_data"
CSV_FILE = os.path.join(CONTACTS_FOLDER, "contacts.csv")

def save_to_file(contact_book):

    if not os.path.exists(CONTACTS_FOLDER):
        os.makedirs(CONTACTS_FOLDER)

    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone_number", "address"])
        writer.writeheader()
        for contact in contact_book.contacts:
            writer.writerow(contact)

def load_from_file(contact_book):

    if not os.path.exists(CSV_FILE):
        return
    with open(CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contact_book.contacts.append({
                "name": row["name"],
                "email": row["email"],
                "phone_number": row["phone_number"],
                "address": row["address"]
            })