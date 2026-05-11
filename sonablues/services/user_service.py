from sqlmodel import select

from sonablues.database.db import get_session
from sonablues.models.user import User
from sonablues.utils.security import hash_password


def create_user(
    username: str,
    password: str,
):
    with get_session() as session:
        existing_user = session.exec(
            select(User).where(
                User.username == username
            )
        ).first()
        if existing_user:
            return False
        user = User(
            username=username,
            password_hash=hash_password(password),
        )
        session.add(user)
        session.commit()
        return True


def get_user_by_username(
    username: str,
):
    with get_session() as session:
        return session.exec(
            select(User).where(
                User.username == username
            )
        ).first()

def add_favorite_song(
    username: str,
    song_slug: str,
):
    with get_session() as session:
        user = session.exec(
            select(User).where(
                User.username == username
            )
        ).first()
        if not user:
            return
        favorites = [
            slug
            for slug in user.favorite_songs.split(",")
            if slug
        ]
        if song_slug not in favorites:
            favorites.append(song_slug)
        user.favorite_songs = ",".join(
            favorites
        )
        session.add(user)
        session.commit()
        

def get_favorite_songs(
    username: str,
) -> list[str]:
    user = get_user_by_username(
        username,
    )
    if not user:
        return []
    return [
        slug
        for slug in user.favorite_songs.split(",")
        if slug
    ]
    

def remove_favorite_song(
    username: str,
    song_slug: str,
):

    with get_session() as session:
        user = session.exec(
            select(User).where(
                User.username == username
            )
        ).first()
        if not user:
            return
        favorites = [
            slug
            for slug in user.favorite_songs.split(",")
            if slug
        ]
        favorites = [
            slug
            for slug in favorites
            if slug != song_slug
        ]
        user.favorite_songs = ",".join(
            favorites
        )
        session.add(user)
        session.commit()
        

def is_favorite_song(
    username: str,
    song_slug: str,
) -> bool:
    favorites = get_favorite_songs(
        username,
    )
    return song_slug in favorites