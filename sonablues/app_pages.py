import reflex as rx

from sonablues.constants import (
    ELECTRIC,
    ACOUSTIC,
)

from sonablues.data.mock.songs_data import SONGS

from sonablues.routes import (
    HOME_ROUTE,
    LOGIN_ROUTE,
    REGISTER_ROUTE,
    PROFILE_ROUTE,
    INSTRUMENTS_ROUTE,
    ELECTRIC_ARTISTS_ROUTE,
    ACOUSTIC_ARTISTS_ROUTE,
    songs_route,
    song_detail_route,
)

from sonablues.pages.home import home_page
from sonablues.pages.login import login_page
from sonablues.pages.register import register_page
from sonablues.pages.profile import profile_page
from sonablues.pages.instruments import instruments_page
from sonablues.pages.artists import artists_page
from sonablues.pages.songs import songs_page
from sonablues.pages.song_detail import song_detail_page
from sonablues.states.profile_state import (
    ProfileState,
)


def register_pages(app: rx.App):

    # Home
    app.add_page(home_page, route=HOME_ROUTE)

    # Auth
    app.add_page(login_page, route=LOGIN_ROUTE)
    app.add_page(register_page, route=REGISTER_ROUTE)

    # Profile
    app.add_page(
        profile_page,
        route=PROFILE_ROUTE,
        on_load=ProfileState.load_favorites,
    )

    # Instruments
    app.add_page(
        instruments_page,
        route=INSTRUMENTS_ROUTE,
    )

    # Artists
    app.add_page(
        lambda: artists_page(ELECTRIC),
        route=ELECTRIC_ARTISTS_ROUTE,
    )

    app.add_page(
        lambda: artists_page(ACOUSTIC),
        route=ACOUSTIC_ARTISTS_ROUTE,
    )

    # Songs pages
    for artist_slug in SONGS.keys():
        app.add_page(
            lambda artist_slug=artist_slug: songs_page(
            artist_slug,
        ),
            route=songs_route(artist_slug),
        )

    # Song detail pages
    for artist_songs in SONGS.values():
        for song in artist_songs:
            app.add_page(
                lambda song_slug=song.slug: song_detail_page(song_slug),
                route=song_detail_route(song.slug),
            )