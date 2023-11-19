import random
from sqlalchemy.orm import sessionmaker
from model import Movies, PlayerScores, engine
from assets.art import logo, vs
from typing import Type
from playerscores_operations import add_highscore, get_highscores
from movies_operations import add_all_movies, get_all_movies, add_movie, edit_movie
from utils.utils import clear_screen, compare

Session = sessionmaker(bind=engine)
session = Session()

all_movies: list[Movies] = get_all_movies()

if len(all_movies) == 0:
    add_all_movies()


def assign_random_movie() -> Type[Movies]:  # +
    return session.query(Movies).get(random.randint(1, len(all_movies)))


def play_higher_lower(nickname) -> None:
    playing_game: bool = True
    while playing_game:
        score: int = 0
        still_guessing: bool = True

        while still_guessing:
            clear_screen()
            print(logo)

            movie1: Type[Movies] = assign_random_movie()
            movie2: Type[Movies] = assign_random_movie()

            while True:
                if movie1 == movie2:
                    movie2: Type[Movies] = assign_random_movie()
                else:
                    break

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
                        print("Invalid Input")
                        continue

                    if compare(movie1.rating, movie2.rating, user_guess):
                        score += 1
                        break
                    else:
                        still_guessing: bool = False
                        break

                except ValueError:
                    print("Invalid Input")

        add_highscore(nickname, score)
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
print(logo)
while True:
    user_nickname: str = input('Enter your nickname:\n')
    if user_nickname != '' and ' ' not in user_nickname:
        break
    else:
        print('Nickname cannot be empty or have multiple words')

while True:
    clear_screen()
    print(logo)
    if user_nickname == 'admin':
        print('\n1. Play the game'
              '\n2. Highscores'
              '\n3. Print all movies'
              '\n4. Edit a movie'
              '\n5. Add new movie'
              '\nq - Quit')
    else:
        print('\n1. Play the game'
              '\n2. Highscores'
              '\nq - Quit')

    selection = input('\n>>> ')
    if selection == 'q':
        print("Program Exit Successful.")
        exit()

    if selection not in ('1', '2', '3', '4', '5') and user_nickname == 'admin':
        print("Invalid Input")
        continue
    elif selection not in ('1', '2') and user_nickname != 'admin':
        print("Invalid Input")
        continue

    if selection == '1':
        clear_screen()
        play_higher_lower(user_nickname)
    elif selection == '2':
        clear_screen()
        print(logo)
        highscores: list[PlayerScores] = get_highscores()
        print('\n----------HIGHSCORES----------')
        for count, player_score in enumerate(highscores, 1):
            print(f'{count}. {player_score.nickname} - {player_score.score}')
        input('\nENTER --> Back to menu')
    elif selection == '3':
        clear_screen()
        print(logo)
        print('\n----------MOVIES----------')
        for movie in all_movies:
            print(f'ID: {movie.id} | name: {movie.name} | release year: {movie.release_year} | rating: {movie.rating}')
        input('\nENTER --> Back to menu')
    elif selection == '4':
        clear_screen()
        print(logo)
        print('\n----------EDIT MOVIE----------')
        while True:
            try:
                print("NOTE: You can check the movie ID's by selecting menu option number 3")
                movie_id: int = int(input('Enter ID of the movie you would like to edit (egz. 1): '))
                break
            except ValueError:
                print('Incorrect number of id, for egz.: 1')

        print('Which part would you like to edit?')
        print('\n1. Name'
              '\n2. Release year'
              '\n3. Rating'
              '\nb - Back to main menu')

        selected = input('\n>>> ')

        if selected == 'b':
            continue

        if selected not in ('1', '2', '3'):
            print('Invalid input')
            continue

        new_value: str | float = ''

        if selected == '1':
            new_value: str = input(f'Enter a new movie name value: ')
        elif selected == '2':
            while True:
                new_value: str = input(f'Enter a new release year value: ')
                if (len(new_value) == 4) and (new_value.isdigit()) and (new_value[:2] in ('20', '19', '18')):
                    break
                else:
                    print('Enter a correct year, for egz.: 1972 \n')
        elif selected == '3':
            while True:
                try:
                    new_value: float = float(input('Enter a new rating value (egz: 9.2): '))
                    break
                except ValueError:
                    print('Invalid rating value, should be for egz.: 9.2:')

        if new_value != '':
            edit_movie(movie_id, selected, new_value)
        else:
            print('New value cannot be empty')

        input('\nENTER --> Back to menu')

    elif selection == '5':
        clear_screen()
        print(logo)
        print('\n----------ADD MOVIE----------')
        name: str = input('Enter a name of the movie (egz. The Godfather): ')
        while True:
            year: str = input('Enter release year of the movie (egz. 1972): ')
            if (len(year) == 4) and (year.isdigit()) and (year[:2] in ('20', '19', '18')):
                break
            else:
                print('Enter a correct year, for egz.: 1972 \n')
        while True:
            try:
                rating: float = float(input('Enter movie rating (egz. 9.2): '))
                break
            except ValueError:
                print('Invalid rating value, should be for egz.: 9.2:')
        add_movie(name, year, rating)
        input('\nENTER --> Back to menu')
    else:
        print("Invalid Input")

session.close()
