from sqlalchemy.orm import sessionmaker
from model import Movies, engine
from assets.movie_list import movies

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    for name, year, rating in movies:
        session.add(Movies(name, year, rating))

session.commit()
session.close()
