from sonablues.data.mock.artists_data import ARTISTS


ARTISTS_BY_SLUG = {
    artist.slug: artist
    for instrument_artists in ARTISTS.values()
    for artist in instrument_artists
}