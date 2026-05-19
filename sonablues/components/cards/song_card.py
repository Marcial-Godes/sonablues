import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.data.models.song_model import (
    Song,
)
from sonablues.components.ui import (
    media_card,
    cover_image,
    badge_group,
    app_badge,
    favorite_button,
    card_link,
    stack_start,
    title_text,
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
                        app_badge(
                            song.difficulty,
                            variant="difficulty",
                        ),

                        app_badge(
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