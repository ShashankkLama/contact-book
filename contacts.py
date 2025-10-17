import json
import os

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"✅ Added contact: {name}")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts found.")
        else:
            print("\n📇 Contact List:")
            for name, info in self.contacts.items():
                print(f"{name} → Phone: {info['phone']}, Email: {info['email']}")

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"🔍 Found: {name} → Phone: {info['phone']}, Email: {info['email']}")
        else:
            print("❌ Contact not found.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]["phone"] = phone
            if email:
                self.contacts[name]["email"] = email
            print(f"✅ Updated contact: {name}")
        else:
            print("❌ Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"🗑️ Deleted contact: {name}")
        else:
            print("❌ Contact not found.")

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump(self.contacts, file)
        print("💾 Contacts saved successfully!")

    def load_from_file(self, filename="contacts.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.contacts = json.load(file)
            print("📂 Contacts loaded successfully.")
        else:
            print("🆕 No saved contacts found. Starting fresh.")


def main():
    contact_book = ContactBook()
    contact_book.load_from_file()  # Load contacts if available

    while True:
        print("\n📖 Contact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("Enter new phone (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            contact_book.update_contact(name, phone if phone else None, email if email else None)

        elif choice == "5":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            contact_book.save_to_file()
            print("👋 Exiting Contact Book. Have a great day!")
            break

        else:
            print("❌ Invalid option! Please choose a valid option.")


if __name__ == "__main__":
    main()
