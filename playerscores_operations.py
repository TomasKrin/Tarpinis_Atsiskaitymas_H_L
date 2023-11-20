from sqlalchemy import desc
from model import PlayerScores


def add_highscore(session, user_nickname, user_score) -> None:
    all_scores: list[PlayerScores] = session.query(PlayerScores).order_by(desc(PlayerScores.score)).all()

    if len(all_scores) < 10:
        session.add(PlayerScores(user_nickname, user_score))
    elif all_scores[-1].score < user_score:
        all_scores[-1].nickname = user_nickname
        all_scores[-1].score = user_score

    session.commit()


def get_highscores(session) -> list[PlayerScores]:
    return session.query(PlayerScores).order_by(desc(PlayerScores.score)).all()
