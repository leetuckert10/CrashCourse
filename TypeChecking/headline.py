# headline.py


def headline(text: str, center: bool = False) -> str:
    ret_str: str
    if center:
        ret_str = f" {text.title()} ".center(50, "*")
    else:
        ret_str = f"{text.title()}\n{'-' * len(text)}"
        
    return ret_str


print(headline("Terry's Type Checking", True))
