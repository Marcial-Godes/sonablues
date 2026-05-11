import reflex as rx

from sonablues.constants import (
    ARTISTS_TITLE,
)

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.cards.artist_card import (
    artist_card,
)

from sonablues.components.ui.page_title import (
    page_title,
)

from sonablues.services.artist_service import (
    get_artists_by_instrument,
)

from sonablues.styles.spacing import(
    LARGE_GAP,
    SECTION_GAP
)


def artists_page(
    instrument_slug: str,
) -> rx.Component:

    artists = get_artists_by_instrument(
        instrument_slug,
    )

    return base_layout(

        rx.vstack(

            page_title(
                ARTISTS_TITLE,
            ),

            rx.grid(

                *[
                    artist_card(artist)
                    for artist in artists
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