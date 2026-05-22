import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.components.ui.text import (
    title_text,
)

from sonablues.components.ui.primitives.badge import badge
from sonablues.components.ui.navigation.card_link import card_link
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.song.favorite_button import (
    favorite_button,
)

from sonablues.components.song.difficulty_badge import (
    difficulty_badge,
)

from sonablues.components.ui.primitives import (
    badge_group,
)
from sonablues.components.ui.cards import (
    media_card,
)
from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.styles.tokens import (
    CARD_IMAGE_HEIGHT_MD,
    SONG_CARD_MIN_HEIGHT,
    TITLE_SIZE_CARD,
    INLINE_GAP,
    CONTENT_GAP,
)


def song_card(
    song: Song,
) -> rx.Component:
    return rx.box(
        card_link(
            media_card(
                rx.box(
                    favorite_button(
                        song.slug,
                        compact=True,
                    ),
                    position="absolute",
                    top="16px",
                    right="16px",
                    z_index="10",
                ),

                cover_image(
                    src=song.image,
                    height=CARD_IMAGE_HEIGHT_MD,
                ),

                stack_start(
                    title_text(
                        song.title,
                        size=TITLE_SIZE_CARD,
                    ),

                    rx.hstack(
                        difficulty_badge(
                            song.difficulty,
                        ),

                        badge(
                            song.tuning,
                        ),

                        spacing=INLINE_GAP,
                        wrap="wrap",
                    ),

                    badge_group(
                        song.techniques,
                        size="1",
                    ),
                    spacing=CONTENT_GAP,
                ),
                min_height=SONG_CARD_MIN_HEIGHT,
                position="relative",
            ),
            href=song_detail_route(
                song.slug,
            ),
        ),
    )