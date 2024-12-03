def search_contacts(contact_book):
    query = input("Enter name or email to search: ")
    print(contact_book.search_contacts(query))