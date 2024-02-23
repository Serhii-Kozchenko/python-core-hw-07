from decorators import input_error

@ input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@ input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact has already been added"
    
    else:
        contacts[name] = phone
        return "Contact added."

@ input_error
def change_phone(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    else:
         contacts[name] = phone

    return "Contact changed"

@ input_error
def show_phone(args, contacts):
    name, *_ = args
    result = contacts[name]
    return result

@ input_error
def delete_phone(args, contacts):
    name, *_ = args
    del contacts[name]

    return "Contact deleted"

@ input_error
def clear_contacts(contacts):

    contacts.clear()
    return "Contacts clear"

@ input_error
def show_all(contacts):
    if not contacts:
        return "Contacts is empty"
    return f"Contacts: {contacts}"
