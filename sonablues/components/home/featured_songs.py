import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.services.song_service import (
    get_featured_songs,
)

from sonablues.styles.tokens import (
    FEATURED_CARD_IMAGE_HEIGHT,
    SECTION_PADDING_Y,
    )
from sonablues.components.ui import (
    section_header,
    surface,
    cover_image,
    title_text,
    secondary_text,
    responsive_grid,
    app_badge,
    card_link,
    stack_start,
    stack_section,
)


def song_card(
    image_src: str,
    title: str,
    artist: str,
    difficulty: str,
    slug: str,
) -> rx.Component:
    return card_link(
        surface(
            stack_section(
                cover_image(
                    src=image_src,
                    height=FEATURED_CARD_IMAGE_HEIGHT,
                    object_position="center top",
                ),
                stack_start(
                    app_badge(
                        difficulty,
                        variant="difficulty",
                    ),
                    title_text(
                        title,
                        size="5",
                        line_height="1.1",
                    ),
                    secondary_text(
                        artist,
                        size="3",
                    ),
                    spacing="1",
                ),
            ),
            padding={
                "base": "0.75rem",
                "md": "1rem",
            },
            width="100%",
            overflow="hidden",
            hoverable=True,
        ),
        href=song_detail_route(slug),
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
                lambda song: song_card(
                    song.image,
                    song.title,
                    song.artist,
                    song.difficulty,
                    song.slug,
                ),
            ),
        ),
        padding_y=SECTION_PADDING_Y,
        margin_top={
            "base": "1.5rem",
            "lg": "0",
        },
    )