import random
from sqlalchemy.orm import sessionmaker
from model import Movies, PlayerScores, engine
from assets.art import logo, vs
import os

Session = sessionmaker(bind=engine)
session = Session()


def clear_screen():  # +
    os.system('cls' if os.name == 'nt' else 'clear')


def assign_random_movie():  # +
    all_movies = session.query(Movies).all()
    return session.query(Movies).get(random.randint(1, len(all_movies)))


def compare(movie1, movie2, user_input):  # +
    higher = 0

    if movie1.rating > movie2.rating:
        higher = 1
    elif movie1.rating < movie2.rating:
        higher = 2

    if higher == user_input:
        return True
    else:
        return False


def play_higher_lower():
    # reikia implementuot update ir instert jeigu jungiasi user_nickname - admin
    # padaryti highscore sistema, kad saugotu top10 scoru: username - score
    playing_game = True
    user_nickname = input('Enter your nickname:\n')

    while playing_game:
        score = 0
        still_guessing = True

        while still_guessing:
            clear_screen()
            print(logo)

            movie1 = assign_random_movie()
            movie2 = assign_random_movie()

            if score > 0:
                movie1 = movie2
                movie2 = assign_random_movie()

                if movie1 == movie2:
                    movie2 = assign_random_movie()

            print(f'Movie name: {movie1.name} - Release year: {movie1.release_year}')
            print(vs)
            print(f'Movie name: {movie2.name} - Release year: {movie2.release_year}')

            print('-' * 50)
            print(f'Your current score: {score}')
            print('-' * 50)
            # Padaryti loopa jeigu iveda neteisinga numeriuka, kad leistu ivesti dar karta
            try:
                user_guess = int(input('Enter which movie has a higher rating (1/2): '))
                if compare(movie1, movie2, user_guess):
                    score += 1
                else:
                    still_guessing = False
            except ValueError:
                print('Incorrect Option')
                still_guessing = False

        play_again = input('Want to Play Again? (y/n): ').lower()

        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing_game = False
            clear_screen()
            print("Game Exited Successfully")
        else:
            playing_game = False
            print("Invalid Input Taken as no.")


want_to_play = input("Do you want to play Higher Lower? (y/n)\n").lower()
if want_to_play == 'y':
    clear_screen()
    play_higher_lower()
elif want_to_play == 'n':
    print("Program Exit Successful.")
    exit()
else:
    print("Invalid Input, Program Exited.")

session.commit()
session.close()
