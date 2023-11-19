import os


def clear_screen() -> None:  # +
    os.system('cls' if os.name == 'nt' else 'clear')


def compare(rating1: float, rating2: float, user_input: int) -> bool:  # +
    higher: int = 0

    if rating1 > rating2:
        higher = 1
    elif rating1 < rating2:
        higher = 2

    if higher == user_input:
        return True
    else:
        return False
