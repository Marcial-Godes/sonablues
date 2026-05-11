from sonablues.data.mock.artists_data import ARTISTS
from sonablues.data.mock.artist_indexes import ARTISTS_BY_SLUG

from sonablues.data.models.artist_model import Artist


def get_artist(artist_slug: str) -> Artist | None:
    return ARTISTS_BY_SLUG.get(artist_slug)


def get_artists_by_instrument(instrument_slug: str) -> list[Artist]:
    return ARTISTS.get(instrument_slug, [])