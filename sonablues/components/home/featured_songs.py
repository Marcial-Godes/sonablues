import reflex as rx

from sonablues.services.song_service import (
    get_featured_songs,
)

from sonablues.components.song import (
    song_preview_card,
)

from sonablues.components.ui.sections import (
    section_header,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
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
                lambda song: song_preview_card(song),
            )
        )
    )