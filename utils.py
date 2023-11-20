import os


def clear_screen() -> None:  # +
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(rating1: float, rating2: float, user_input: int) -> bool:  # +
    higher: int = 0

    if rating1 >= rating2:
        higher = 1
    elif rating1 <= rating2:
        higher = 2

    if higher == user_input:
        return True
    else:
        return False


def check_inp_float(msg: str) -> float:
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print('Invalid rating value, should be for egz.: 9.2:')


def check_inp_empty_str(msg: str) -> str:
    while True:
        name: str = input(msg)
        if name != '':
            return name
        else:
            print('Field, cannot be empty')
            continue


def check_inp_year(msg: str) -> str:
    while True:
        year: str = input(msg)
        if (len(year) == 4) and (year.isdigit()) and (year[:2] in ('20', '19', '18')):
            return year
        else:
            print('Enter a correct year, for egz.: 1972 \n')
