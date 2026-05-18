import reflex as rx
from sonablues.data.models.artist_model import (
    Artist,
)
from sonablues.routes import (
    songs_route,
)
from sonablues.components.ui import (
    media_card,
    cover_image,
    card_link,
    stack_start,
    title_text,
    secondary_text,
)
from sonablues.styles.tokens import (
    CARD_IMAGE_HEIGHT_LG,
    ARTIST_CARD_MIN_HEIGHT,
    TITLE_SIZE_CARD,
    CONTENT_GAP,
    TEXT_SIZE_SECONDARY,
)


def artist_card(
    artist: Artist,
) -> rx.Component:
    return card_link(
        media_card(
            cover_image(
                src=artist.image,
                height=CARD_IMAGE_HEIGHT_LG,
            ),
            stack_start(
                title_text(
                    artist.name,
                    size=TITLE_SIZE_CARD,
                ),
                secondary_text(
                    artist.description,
                    size=TEXT_SIZE_SECONDARY,
                ),
                spacing=CONTENT_GAP,
            ),
            min_height=ARTIST_CARD_MIN_HEIGHT,
        ),
        href=songs_route(
            artist.slug,
        ),
    )