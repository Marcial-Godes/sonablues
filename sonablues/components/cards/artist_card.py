import reflex as rx
from sonablues.data.models.artist_model import Artist
from sonablues.routes import (
    songs_route,
)
from sonablues.components.ui import (
    surface,
    cover_image,
    muted_text,
)
from sonablues.styles.theme import (
    TEXT_COLOR,
)
from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
    MEDIUM_GAP,
)


def artist_card(artist: Artist) -> rx.Component:
    return rx.link(
        surface(
            rx.vstack(
                cover_image(
                    src=artist.image,
                    height="220px",
                ),
                rx.vstack(
                    rx.heading(
                        artist.name,
                        size="5",
                        color=TEXT_COLOR,
                    ),
                    muted_text(
                        artist.description,
                        size="3",
                    ),
                    spacing=EXTRA_SMALL_GAP,
                    align="start",
                    width="100%",
                ),
                spacing=MEDIUM_GAP,
                align="start",
            ),
            width="100%",
            hoverable=True,
        ),
        href=songs_route(artist.slug),
        width="100%",
        text_decoration="none",
    )