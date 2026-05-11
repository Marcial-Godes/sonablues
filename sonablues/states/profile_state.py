# sonablues/states/profile_state.py

import reflex as rx
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.services.user_service import (
    get_favorite_songs,
)
from sonablues.data.mock.song_indexes import (
    SONGS_BY_SLUG,
)
from sonablues.states.auth_state import (
    AuthState,
)


class ProfileState(rx.State):
    favorite_songs: list[Song] = []

    async def load_favorites(self):
        auth_state = await self.get_state(
            AuthState,
        )
        if not auth_state.logged_user:
            self.favorite_songs = []
            return
        favorite_slugs = get_favorite_songs(
            auth_state.logged_user,
        )
        self.favorite_songs = [
            SONGS_BY_SLUG[slug]
            for slug in favorite_slugs
            if slug in SONGS_BY_SLUG
        ]