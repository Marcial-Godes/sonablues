import reflex as rx

from sonablues.services.song_service import (
    get_songs_by_artist,
)

from sonablues.data.models.song_model import (
    Song,
)


class SongSearchState(rx.State):

    search_text: str = ""

    filtered_songs: list[Song] = []

    all_songs: list[Song] = []

    def load_songs(
        self,
        artist_slug: str,
    ):

        songs = get_songs_by_artist(
            artist_slug,
        )

        self.all_songs = songs

        self.filtered_songs = songs

    def set_search(
        self,
        value: str,
    ):

        self.search_text = value

        query = (
            value
            .strip()
            .lower()
        )

        if not query:

            self.filtered_songs = (
                self.all_songs
            )

            return

        self.filtered_songs = [
            song
            for song in self.all_songs
            if (
                query in song.title.lower()
                or query in str(
                    song.difficulty
                ).lower()
            )
        ]