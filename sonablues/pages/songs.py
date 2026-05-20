import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    page_container,
)
from sonablues.components.cards.ui import (
    song_card,
)
from sonablues.components.search import (
    song_search_input,
)
from sonablues.components.ui import (
    empty_state,
    responsive_grid,
    page_header,
)
from sonablues.components.ui.layout import (
    content_stack,
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
            content_stack(
                page_header(
                    title=artist.name,
                    description=artist.description,
                ),
                song_search_input(),
                responsive_grid(
                    *[
                        song_card(song)
                        for song in songs
                    ],
                ),
            )
        )
    )