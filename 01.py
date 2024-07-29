from model.addressBook import AddressBook
from model.record import Record

def print_all():
    print("\nAddress book:")
    for _, record in book.data.items():
        print(record)
    print()
    
#--------------------------------

try:
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("7777777777")
    john_record.add_birthday("30.07.1990")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("11.03.2001")
    book.add_record(jane_record)

    alex_record = Record("Alex")
    alex_record.add_phone("1112223378")
    alex_record.add_birthday("02.08.1997")
    book.add_record(alex_record)

    print_all()

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    john.remove_phone("7777777777")

    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  

    book.delete("Jane")

    print_all()


except Exception as e:
    print(f'Error: {e}')

print(book.get_upcoming_birthdays())
