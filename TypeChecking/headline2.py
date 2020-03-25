# headline.py
# This demonstrates two methods of using type comments.


def headline(
        text,           # type: str
        width=80,       # type: int
        fill_char='-',  # type: str
        ):              # type(...) -> str
    ret_string = ""     # type: str
    ret_string = f" {text.title()} ".center(width, fill_char)
    return ret_string


def headline2(text, width=80, fill_char='*'):
    # type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)


print(headline("type comments work", 40))
print(headline2("type comments work", 50))
