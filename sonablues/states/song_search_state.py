import reflex as rx
from sonablues.services.song_service import (
    get_songs_by_artist,
)


class SongSearchState(rx.State):
    search_text: str = ""
    def set_search(
        self,
        value: str,
    ):
        self.search_text = value
    def filtered_songs(
        self,
        artist_slug: str,
    ):
        songs = get_songs_by_artist(
            artist_slug,
        )
        query = self.search_text.strip().lower()
        if not query:
            return songs

        return [
            song
            for song in songs
            if (
                query in song.title.lower()
                or
                query in str(song.difficulty).lower()
                or
                any(
                    query in technique.lower()
                    for technique in song.techniques
                )
            )
        ]