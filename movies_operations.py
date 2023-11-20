from model import Movies
from assets.movie_list import movies


def add_all_movies(session) -> None:
    for name, year, rating in movies:
        session.add(Movies(name, year, rating))


def get_all_movies(session) -> list[Movies]:
    return session.query(Movies).all()


def get_movie(session, movie_id: int) -> Movies:
    return session.query(Movies).get(movie_id)


def add_movie(session, name: str, release_year: str, rating: float) -> None:
    filtered_movies: list[Movies] = session.query(Movies).filter_by(name=name, release_year=release_year).all()
    if not filtered_movies:
        session.add(Movies(name, release_year, rating))
        session.commit()
        print(f'\nMovie: {name}({release_year}) - {rating}, was added')
    else:
        print(f'\nMovie: {name}({release_year}) - {rating}, already exists')


def edit_movie(session, movie_id: int, choice: str, new_value: str | float) -> None:
    movie_for_edit: Movies = session.query(Movies).get(movie_id)
    if choice == '1':
        movie_for_edit.name = new_value
    elif choice == '2':
        movie_for_edit.release_year = new_value
    elif choice == '3':
        movie_for_edit.rating = new_value
    session.commit()
    edited: Movies = session.query(Movies).get(movie_id)
    print(f'Edited movie: ID: {edited.id} | {edited.name}({edited.release_year}) - {edited.rating}')
