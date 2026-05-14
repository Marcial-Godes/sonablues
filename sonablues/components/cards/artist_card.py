import reflex as rx
from sonablues.data.models.artist_model import (
    Artist,
)
from sonablues.components.ui import (
    surface,
    cover_image,
    card_link,
    stack_start,
    stack_section,
    title_text,
    secondary_text,
)
from sonablues.routes import (
    songs_route,
)
from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
)
from sonablues.styles.tokens import (
    SONG_CARD_IMAGE_HEIGHT,
)


def artist_card(
    artist: Artist,
) -> rx.Component:
    return card_link(
        surface(
            stack_section(
                cover_image(
                    src=artist.image,
                    height=SONG_CARD_IMAGE_HEIGHT,
                ),
                stack_start(
                    title_text(
                        artist.name,
                        size="5",
                    ),
                    secondary_text(
                        artist.description,
                        size="3",
                    ),
                    spacing=EXTRA_SMALL_GAP,
                ),
            ),
            width="100%",
            hoverable=True,
        ),
        href=songs_route(
            artist.slug,
        ),
    )