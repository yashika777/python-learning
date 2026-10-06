# Contact Book (Dictionary)
# Create a contact book application with the following features:
#  Contact book structure
# contacts = {}
# Features to implement:
# 1. Add new contact (name: phone number)
# 2. Search contact by name
# 3. Update phone number
# 4. Delete contact
# 5. Display all contacts
# 6. Count total contacts
contacts = {
    'Rahul': 7483920769,
    'Raghav': 5647839210,
    'Yashika': 9813283858
}
while True:
    print("""
--- Contact Book Menu ---
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Display All Contacts
6. Count Total Contacts
7. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = int(input("Enter phone number: "))
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == 2:
        name = input("Enter name to search: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == 3:
        name = input("Enter name to update: ")

        if name in contacts:
            phone = int(input("Enter new phone number: "))
            contacts[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == 4:
        name = input("Enter contact to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == 5:
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 6:
        print("Total contacts:", len(contacts))

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice.")

