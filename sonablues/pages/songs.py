import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
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
    secondary_text,
    responsive_grid,
    stack_start,
    stack_section,
)
from sonablues.services.song_service import (
    get_songs_by_artist,
)
from sonablues.services.artist_service import (
    get_artist,
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
        page_container(
            stack_section(
                stack_start(
                    page_title(
                        artist.name,
                    ),
                    secondary_text(
                        artist.description,
                    ),
                ),
                song_search_input(),
                responsive_grid(
                    *[
                        song_card(song)
                        for song in songs
                    ],
                ),
                align="stretch",
            )
        )
    )