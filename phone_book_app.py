import os

phonebook_data = [
    {
        "name": "Melissa",
        "number": "404-235-5428"
    },
    {
        "name": "Joe",
        "number": "404-235-2125"
    },
    {
        "name": "Mike",
        "number": "770-134-2229"
    },
    {
        "name": "Igor",
        "number": "770-233-3461"
    }
]


def look_up_entry(name):
    phone_num_dict = [num_dict for num_dict in phonebook_data if name in num_dict.values()]
    if not phone_num_dict:
        os.system("clear")
        print ("Not in the list")
        print ("Try again!\n")
        main()
    else:
        return phone_num_dict


def set_an_entry(name, phone_number):
    new_dict = {"name": name, "phone_number": phone_number}
    phonebook_data.append(new_dict)
    print ("%s has been added.\n" % name)


def Delete_an_entry(name):
    for n in phonebook_data:
        if name in n.values():
            phonebook_data.remove(n)



def list_all_entry(phone_book):
    print (phone_book)


def search_entry(data):
    phone_num_dict = [num_dict for num_dict in phonebook_data if data in num_dict.values()]
    if not phone_num_dict:
        return ("Not in the list")
    else:
        return phone_num_dict

def main():
    run_app = True
    while run_app:
        print ("""Electronic Phone Book
        =====================
        1. Look up an entry
        2. Set an entry
        3. Delete an entry
        4. List all entries
        5. Search for an entry
        6. Quit
        """)
        user_input = input("What do you want to do (1-5)?\n")
        try:
            convert_user = int(user_input)
        except ValueError:
            os.system("clear")  # passing any linux command line you want
            print ("You must enter a number!\n")
        else:
            if (convert_user == 1):
                print ("you choose 1")
                name_user = input("Who do you want to look up?\n")
                print(look_up_entry(name_user))

            elif (convert_user == 2):
                print ("you choose 2")
                print ("Please enter a name:\n")
                user_name = input("> ")
                print ("Please enter a phone number:\n")
                user_number = input("> ")

                set_an_entry(user_name, user_number)

            elif (convert_user == 3):
                print ("you choose 3")
                del_user = input("Who do you want to get rid of?\n ")
                Delete_an_entry(del_user)
                print ("You did it\n")
            elif (convert_user == 4):
                print ("you choose 4")
                list_all_entry(phonebook_data)
            elif (convert_user == 5):
                print ("you choose 5")
                data_user = input("Enter a name or phone number:\n")
                print(look_up_entry(data_user))
            elif (convert_user == 6):
                print ("exit")
                run_app = False
main()
