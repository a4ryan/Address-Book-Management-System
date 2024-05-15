!pip install sqlite3
import sqlite3

# Function to create a new contact
def create_contact(conn, name, email, phone):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    print("Contact added successfully.")

# Function to display all contacts
def display_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(contact)

# Main function
def main():
    # Connect to the SQLite database (creates a new one if not exists)
    conn = sqlite3.connect('address_book.db')

    # Create a contacts table if not exists
    conn.execute('''CREATE TABLE IF NOT EXISTS contacts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             email TEXT,
             phone TEXT);''')

    while True:
        print("\nAddress Book")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            create_contact(conn, name, email, phone)
        elif choice == '2':
            display_contacts(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection when done
    conn.close()

if __name__ == "__main__":
    main()
