

def generate_password(
    password_length: int = 8,
    has_symbols: bool = False,
    has_uppercase: bool = False,
    ignored_chars: list = [],
    allowed_chars: list = []
) -> str:
    """Generates a random password.

    The password will be exactly `password_length` characters.
    If `has_symbols` is True, the password will contain at least one symbol,
    such as #, !, or @. If `has_uppercase` is True, the password will contain
    at least one upper case letter.
    """
    import random
    import string

    password = ''
    num_chars_to_add = password_length

    if password_length >= 1000000:
        UserWarning('password_length cannot equal or exceed 1,000,000.')

    if (ignored_chars != []
            and allowed_chars != []):
        raise UserWarning('ignored_chars or allowed_chars must be empty.')
    elif ignored_chars != []:
        _choices = list(set(string.ascii_lowercase) - set(ignored_chars))
        choices = ''.join(_choices)
    elif allowed_chars != []:
        choices = ''.join(allowed_chars)
    elif (ignored_chars == []
            and allowed_chars == []):
        choices = string.ascii_lowercase

    if allowed_chars == []:
        if has_symbols:
            _allowed_punct = set(string.punctuation) - set(ignored_chars)
            allowed_punct = ''.join(_allowed_punct)
            password += random.choice(allowed_punct)
            num_chars_to_add -= 1
            choices += allowed_punct
        if has_uppercase:
            _allowed_up = set(string.ascii_uppercase) - set(ignored_chars)
            allowed_up = ''.join(_allowed_up)
            password += random.choice(allowed_up)
            num_chars_to_add -= 1
            choices += allowed_up

    for i in range(num_chars_to_add):
        password += random.choice(choices)

    def scrambler(word):
        _word = list(word)
        random.shuffle(_word)
        new_word = ''.join(_word)
        return new_word

    password_final = scrambler(password)

    return password_final


if __name__ == '__main__':
    print(generate_password(8, True, True))
