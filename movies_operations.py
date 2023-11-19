from sqlalchemy.orm import sessionmaker
from model import Movies, engine
from assets.movie_list import movies

Session = sessionmaker(bind=engine)
session = Session()


def add_all_movies() -> None:
    for name, year, rating in movies:
        session.add(Movies(name, year, rating))


def get_all_movies() -> list[Movies]:
    return session.query(Movies).all()


def add_movie(name: str, release_year: str, rating: float) -> None:
    filtered_movies: list[Movies] = session.query(Movies).filter_by(name=name, release_year=release_year).all()
    if not filtered_movies:
        session.add(Movies(name, release_year, rating))
        session.commit()
        print(f'\nMovie: {name}({release_year}) - {rating}, was added')
    else:
        print(f'\nMovie: {name}({release_year}) - {rating}, already exists')


def edit_movie(movie_id: int, choice: str, new_value: str | float) -> None:
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


session.close()
