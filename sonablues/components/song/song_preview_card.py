import reflex as rx

from sonablues.components.ui.navigation.card_link import card_link
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.ui.text import (
    secondary_text,
    title_text,
)

from sonablues.components.ui.layout import (
    content_stack,
)

from sonablues.styles.tokens import (
    CONTENT_GAP,
    TITLE_SIZE_CARD,
)

from sonablues.data.models.song_model import Song


def song_preview_card(
    song: Song,
) -> rx.Component:
    return card_link(
        content_stack(
            cover_image(
                song.image,
                alt=song.title,
                height="220px",
            ),

            title_text(
                song.title,
                size=TITLE_SIZE_CARD,
            ),

            secondary_text(
                song.artist,
            ),

            secondary_text(
                song.difficulty,
            ),

            spacing=CONTENT_GAP,
        ),
        href=f"/song/{song.slug}",
    )