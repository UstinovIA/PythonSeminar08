phone_book = []
path = 'PB_console\phones.txt'

class Contact:
    
    current_uid = 1

    def __init__(self, name, phone, comment):
        self.uid = Contact.current_uid
        self.name = name
        self.phone = phone
        self.comment = comment


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    max_uid = 0
    for contact in data:
        input_data = Contact()
        input_data.uid, input_data.name, input_data.phone, input_data.comment = contact.strip().split(':')
        phone_book.append(input_data)
        if(input_data.uid > max_uid):
            max_uid = input_data
    Contact.current_uid = max_uid


def add_contact(new: dict):
    input_contact = Contact()
    Contact.current_uid = Contact.current_uid + 1
    input_contact.uid = Contact.current_uid
    input_contact.name = dict.get('name')
    input_contact.phone = dict.get('phone')
    input_contact.comment = dict.get('comment')
    phone_book.append(input_contact)


def search(word: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for key, value in contact.items():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result


def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            phone_book[index - 1][key] = field
