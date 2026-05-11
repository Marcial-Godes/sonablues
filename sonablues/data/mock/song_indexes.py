from sonablues.data.mock.songs_data import SONGS


SONGS_BY_SLUG = {
    song.slug: song
    for artist_songs in SONGS.values()
    for song in artist_songs
}