from contact_book import ContactBook
from file_operations import save_to_file, load_from_file
from add_contact import add_contact
from view_contacts import view_contacts
from remove_contact import remove_contact
from search_contacts import search_contacts

def main():
    contact_book = ContactBook()
    load_from_file(contact_book)
    print("***************Contact Book Management System************")
    while True:
        print("Operations Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
             if add_contact(contact_book):
                save_to_file(contact_book)

        elif choice == '2':
            view_contacts(contact_book)

        elif choice == '3':
            if remove_contact(contact_book):
                save_to_file(contact_book)

        elif choice == '4':
            search_contacts(contact_book)

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()