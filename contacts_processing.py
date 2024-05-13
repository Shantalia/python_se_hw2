from addressbook import *
import pickle

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

# декоратор для обробки помилки ValueError
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:   
            return "Give me correct name/phone/birthday please."  
        except IndexError:
            return "There is no result. Give me name/phone/birthday please."
    return inner

# функція обробки введеного рядка
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# функція додавання контакту в файл
@input_error
def add_contact(args, book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."

# функція зміни існуючого контакту
@input_error
def change_contact(args, book):
    name, new_phone = args
    for nm in book.data:
        if nm == name:
            book.data[name].edit_phone(new_phone)
            return "Contact changed."
        elif nm != name:
            continue
        else:
            return "No contact with this name!"

# функція виведення існуючого контакту по імені
@input_error
def show_phone(args, book):
    name = args[0]
    return book.find(name)

# функція додавання др контакту
@input_error
def add_birth(args, book):
    name, birthday = args
    for nm in book.data:
        if nm == name:
            book.data[name].add_birthday(birthday)
            return "Birthday added."
        elif nm != name:
            continue
        else:
            return "No contact with this name!"

# функція виведення всіх контактів
@input_error
def show_all(book):
    for key, record in book.data.items():
        print(record)
    return "--------------"   

# функція виведення всіх контактів з ДР на цьому тижні
@input_error
def congrats(book):
    return book.get_upcoming_birthdays()

# функція виведення ДР контакту по імені
@input_error
def show_birthday(args, book):
    name = args[0]
    for nm in book.data:
        if (nm == name) and (book.data[name].birthday):
            return book.data[name].birthday.value
        elif nm != name:
            continue
        else:
            return "No contact with this name or no added birthday!"
