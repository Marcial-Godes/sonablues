from sonablues.data.mock.songs_data import SONGS
from sonablues.data.mock.song_indexes import SONGS_BY_SLUG

from sonablues.data.models.song_model import Song


def get_song(song_slug: str) -> Song | None:
    return SONGS_BY_SLUG.get(song_slug)


def get_songs_by_artist(artist_slug: str) -> list[Song]:
    return SONGS.get(artist_slug, [])

def get_featured_songs():
    featured_slugs = {
        "sloe-gin",
        "spanish-boots",
        "little-wing",
    }

    return [
        song
        for artist_songs in SONGS.values()
        for song in artist_songs
        if song.slug in featured_slugs
    ]