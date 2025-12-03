# Contact Book Application - mnv_godhani 😉

import time

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
        if len(Contact) == 0:
            print("No Contacts Available! ❌")
        else:
            print("----------------------------------------------------------")
            print    ("No  Name    |    Phone       |     Email  ")
            print("----------------------------------------------------------")
            num = 1
            for data in Contact:
                print(num, " ",data["name"], "  |  ", data["phone"], "  |  ", data["Email"])
                num += 1
            print("----------------------------------------------------------")
    elif choice == 2:
        name = input("Enter Name :- ")
        phone = input("Enter Phone Number :- ")
        if len(phone) != 10 or not phone.isdigit():
            print("Invalid Phone Number! ❌")
            continue
        email = input("Enter Email :- ")
        if "@" not in email or "." not in email:
            print("Invalid Email Address! ❌")
            continue
        Contact.append({"name" : name, "phone" : phone, "Email" : email})
        print("----------------------------------------------------------")
        print("Contact Added Successfully! ✅")
    elif choice == 3:
        if len(Contact) < 1:
            print("No Contacts Available! for delete ❌")
            continue
        else:
            print("----------------------------------------------------------")
            print    ("No  Name    |    Phone       |     Email  ")
            print("----------------------------------------------------------")
            num = 1
            for data in Contact:
                print(num, " ",data["name"], "  |  ", data["phone"], "  |  ", data["Email"])
                num += 1
            print("----------------------------------------------------------")
        delete = int(input("Enter Contact Number to Delete :- "))
        Contact.pop(delete - 1)
        print("Contact Deleted Successfully! ✅")
    elif choice == 4:
        print("Exiting Contact Book... 👋")
        time.sleep(3)
        print("🙏 Sitaram 🙏")
        break
    else:
        print("Invalid Choice! ❌")


# Contact Book Application by mnv_godhani 😉
# contact Book allows you to view, add, and delete contacts.
# Each contact consists of a name, phone number, and email address.
# The application runs in a loop until the user chooses to exit.
# It includes basic validation for phone numbers and email addresses.
# Enjoy managing your contacts! 📒📱