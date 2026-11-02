def parse_input(user_input):
    if not user_input.strip():
        return '',

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter user name."

    return inner

@input_error
def add_contact(args, contacts):

    name, phone = args
    contacts[name] = phone
    return 'Contact added.'

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError(name)
    contacts[name] = phone
    return 'Contact updated.'

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    return 'Contact not found.'

@input_error
def show_all(contacts):
    if not contacts:
        return 'No contacts found.'

    return '\n'.join(
        f'{name}: {phone}'
        for name, phone in contacts.items()
    )


def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    commands = {
        '1': 'add',
        '2': 'change',
        '3': 'phone',
        '4': 'all',
        '5': 'exit'

    }

    while True:

        user_input = input(
    '\033[33mEnter a command  or exit/close:\033[0m')

        command, *args = parse_input(user_input)
        command = commands.get(command, command)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
            print('\nChoose a command:\n'
            '1 - add username phone:\n'
            '2 - change username phone\n'
            '3 - phone username\n'
            '4 - show all contacts\n'
            '5 - Exit/Close\n'
            'Your choice: ')
        elif command == 'add':

            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))

        elif command == 'all':
            print(show_all(contacts))

        else:

            print(
                '\n\033[96mCHOOSE A COMMAND:\033[0m\n'
                '\033[32mADD\033[0m \033[32mUSERNAME PHONE\033[0m -> (\033[96mCommand:\033[0m add Anna +380xxxxxxxxx)\n'
                '\033[32mCHANGE\033[0m \033[32mUSERNAME PHONE\033[0m -> (\033[96mCommand:\033[0m change Anna +380xxxxxxxxx)\n'
                '\033[32mPHONE\033[0m \033[32mUSERNAME\033[0m -> (\033[96mCommand:\033[0m phone Anna)\n'
                '\033[32mSHOW ALL CONTACTS\033[0m -> (\033[96mCommand:\033[0m all)\n'
                '\033[32mEXIT/CLOSE\033[0m -> (\033[96mCommand:\033[0m exit/close)\n'
            )


if __name__ == '__main__':
    main()