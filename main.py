import random
import os
from sqlalchemy.orm import sessionmaker
from model import Movies, PlayerScores, engine
from assets.art import logo, vs
from typing import Type
from playerscores_operations import add_highscore, get_highscores
from movies_operations import add_all_movies

Session = sessionmaker(bind=engine)
session = Session()

all_movies: list[Movies] = session.query(Movies).all()

if len(all_movies) == 0:
    add_all_movies()


def clear_screen() -> None:  # +
    os.system('cls' if os.name == 'nt' else 'clear')


def assign_random_movie() -> Type[Movies]:  # +
    return session.query(Movies).get(random.randint(1, len(all_movies)))


def compare(rating1, rating2, user_input) -> bool:  # +
    higher: int = 0

    if rating1 > rating2:
        higher = 1
    elif rating1 < rating2:
        higher = 2

    if higher == user_input:
        return True
    else:
        return False


def play_higher_lower() -> None:
    # reikia implementuot update ir instert jeigu jungiasi user_nickname - admin
    playing_game: bool = True
    user_nickname: str = input('Enter your nickname:\n')

    while playing_game:
        score: int = 0
        still_guessing: bool = True

        while still_guessing:
            clear_screen()
            print(logo)

            movie1: Type[Movies] = assign_random_movie()
            movie2: Type[Movies] = assign_random_movie()

            if score > 0:
                movie1: Type[Movies] = movie2
                movie2: Type[Movies] = assign_random_movie()

                if movie1 == movie2:
                    movie2: Type[Movies] = assign_random_movie()

            print(f'Movie name: {movie1.name} - Release year: {movie1.release_year}')
            print(vs)
            print(f'Movie name: {movie2.name} - Release year: {movie2.release_year}')

            print('-' * 50)
            print(f'Your current score: {score}')
            print('-' * 50)

            while True:
                try:
                    user_guess = int(input('Enter which movie has a higher rating (1/2): '))

                    if user_guess not in (1, 2):
                        print('Incorrect Option')
                        continue

                    if compare(movie1.rating, movie2.rating, user_guess):
                        score += 1
                        break
                    else:
                        still_guessing: bool = False
                        break

                except ValueError:
                    print('Incorrect Option')

        add_highscore(user_nickname, score)
        play_again: str = input('Want to Play Again? (y/n): ').lower()

        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing_game: bool = False
            clear_screen()
            print("Game Exited Successfully")
        else:
            playing_game: bool = False
            print("Invalid Input Taken as no.")


# meniu
want_to_play = input("Do you want to play Higher Lower? (y/n)\n").lower()

if want_to_play == 'y':
    clear_screen()
    play_higher_lower()
elif want_to_play == 'n':
    print("Program Exit Successful.")
    exit()
else:
    print("Invalid Input, Program Exited.")

session.close()
