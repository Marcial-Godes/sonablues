import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.components.ui import (
    media_card,
    cover_image,
    title_text,
    secondary_text,
    app_badge,
    card_link,
)
from sonablues.components.ui.layout import (
    stack_start,
)
from sonablues.styles.tokens import (
    CARD_IMAGE_HEIGHT_MD,
    CARD_PADDING,
    CONTENT_GAP,
    TITLE_SIZE_CARD,
    TEXT_SIZE_SECONDARY,
)


def featured_song_card(
    image_src: str,
    title: str,
    artist: str,
    difficulty: str,
    slug: str,
) -> rx.Component:
    return card_link(
        media_card(
            cover_image(
                src=image_src,
                height=CARD_IMAGE_HEIGHT_MD,
                object_position="center top",
            ),
            stack_start(
                app_badge(
                    difficulty,
                    variant="difficulty",
                ),
                title_text(
                    title,
                    size=TITLE_SIZE_CARD,
                    line_height="1.1",
                ),
                secondary_text(
                    artist,
                    size=TEXT_SIZE_SECONDARY,
                ),
                spacing=CONTENT_GAP,
            ),
            padding=CARD_PADDING,
            overflow="hidden",
        ),
        href=song_detail_route(slug),
    )