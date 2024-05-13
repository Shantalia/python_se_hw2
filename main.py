from contacts_processing import *
from addressbook import *

def main():
    print("Welcome to the assistant bot!")
    book = load_data()
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("There is no command in line!")
            break
        except UnboundLocalError:
            print("There is no command in line! Bye!")
            break

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "add-birthday":
            print(add_birth(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "birthday":
            print(show_birthday(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "congrats":
            print(congrats(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()