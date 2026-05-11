import reflex as rx

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.cards.song_card import (
    song_card,
)

from sonablues.components.search import (
    song_search_input,
)

from sonablues.components.ui import (
    page_title,
    empty_state,
    muted_text,
)

from sonablues.services.song_service import (
    get_songs_by_artist,
)

from sonablues.services.artist_service import (
    get_artist,
)

from sonablues.styles.spacing import (
    SMALL_GAP,
    LARGE_GAP,
    SECTION_GAP,
)


def songs_page(
    artist_slug: str,
) -> rx.Component:

    artist = get_artist(artist_slug)

    if not artist:

        return base_layout(

            empty_state(
                "Artist not found",
            )
        )

    songs = get_songs_by_artist(
        artist_slug,
    )

    return base_layout(

        rx.vstack(

            rx.vstack(

                page_title(
                    artist.name,
                ),

                muted_text(
                    artist.description,
                ),

                spacing=SMALL_GAP,
                align="start",
                width="100%",
            ),

            song_search_input(),

            rx.grid(

                *[
                    song_card(song)
                    for song in songs
                ],

                columns={
                    "base": "1",
                    "md": "2",
                    "lg": "3",
                },

                spacing=LARGE_GAP,
                width="100%",
            ),

            spacing=SECTION_GAP,
            align="start",
            width="100%",
        )
    )