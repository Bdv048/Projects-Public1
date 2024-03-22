import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True

    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits
    new_password: str = ''
    combination_length = 2

    if symbols:
        combination += string.punctuation
        new_password += string.punctuation[secrets.randbelow(len(string.punctuation))]
        combination_length -= 1

    if uppercase:
        combination += string.ascii_uppercase
        new_password += string.ascii_uppercase[secrets.randbelow(len(string.ascii_uppercase))]
        combination_length -= 1

    combination_length += len(combination)


    for _ in range(length - 2):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__ == '__main__':
    for i in range(1, 6):
        new_pass: str = generate_password(length=8, symbols=True, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, S:{contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')