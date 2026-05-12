HOME_ROUTE = "/"
LOGIN_ROUTE = "/login"
REGISTER_ROUTE = "/register"
PROFILE_ROUTE = "/profile"
FAVORITES_ROUTE = "/favorites"

INSTRUMENTS_ROUTE = "/instruments"

ELECTRIC_ARTISTS_ROUTE = "/artists/electric"
ACOUSTIC_ARTISTS_ROUTE = "/artists/acoustic"


def songs_route(artist_slug: str) -> str:
    return f"/songs/{artist_slug}"


def song_detail_route(song_slug: str) -> str:
    return f"/song/{song_slug}"