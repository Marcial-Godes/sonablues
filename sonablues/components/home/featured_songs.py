import reflex as rx

from sonablues.services.song_service import (
    get_featured_songs,
)

from sonablues.components.cards import (
    featured_song_card,
)

from sonablues.components.ui import (
    section_header,
    responsive_grid,
    stack_section,
)


def featured_songs() -> rx.Component:
    return stack_section(
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