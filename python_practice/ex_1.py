def to_int(s):
    number = 0
    if s[0] == '-' and s[1:].isdigit():
        for char in s[1:]:
            number = number * 10 + ord(char) - ord('0')
        return number * (-1)
    elif s.isdigit():
        for char in s:
            number = number * 10 + ord(char) - ord('0')
        return number
    else:
        raise ValueError('Неверный формат строки')


def str_to_int(string: str):
    try:
        return eval(string)
    except (ValueError, SyntaxError, NameError):
        raise ValueError('Неверный формат строки')


numbers = "-1234"
print(str_to_int(numbers))
print(to_int(numbers))