import reflex as rx

from sonablues.services.song_service import (
    get_featured_songs,
)

from sonablues.components.cards.ui import (
    featured_song_card,
)

from sonablues.components.ui import (
    section_header,
    responsive_grid,
)
from sonablues.components.ui.layout import (
    content_stack,
)

def featured_songs() -> rx.Component:
    return content_stack(
        section_header(
            "Canciones destacadas",
            "Aprende algunos de los riffs y canciones más icónicos.",
        ),
        responsive_grid(
            rx.foreach(
                get_featured_songs(),
                lambda song: featured_song_card(
                    song.image,
                    song.title,
                    song.artist,
                    song.difficulty,
                    song.slug,
                ),
            ),
        ),
    )