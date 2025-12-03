print("Hello from Contact-Book/contact_book.py")

Contact = [{"name" : "Manav", "phone" : "1234567890", "Email" : "manavgodhnai88@gmail.com"}]

while True:
    print("\nContact Book Menu:\n")
    print(" 1️⃣  View Contacts")
    print(" 2️⃣  Add Contact")
    print(" 3️⃣  Delete Contact")
    print(" 4️⃣  Exit\n")

    print("-----------------------------")
    choice = int(input("Enter your choice :- "))

    if choice == 1:
        print("----------------------------------------------------------")
        print    ("Name    |    Phone       |     Email  ")
        print("----------------------------------------------------------")
        for data in Contact:
            print(data["name"], "  |  ", data["phone"], "  |  ", data["Email"])

    else:
        print("Invalid Choice! ❌")