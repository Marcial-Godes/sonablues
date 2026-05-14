import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.ui import (
    page_title,
    secondary_text,
    badge_group,
    cover_image,
    app_badge,
    stack_start,
    stack_section,
)
from sonablues.styles.sizes import (
    CONTENT_WIDTH,
)
from sonablues.styles.spacing import (
    SMALL_GAP,
    LARGE_GAP,
    PAGE_GAP,
)
from sonablues.styles.tokens import (
    SONG_HERO_IMAGE_HEIGHT,
    )


def song_hero(
    song: Song,
) -> rx.Component:
    return stack_section(
        cover_image(
            src=song.image,
            height=SONG_HERO_IMAGE_HEIGHT,
            max_width=CONTENT_WIDTH,
        ),
        stack_start(
            page_title(
                song.title,
            ),
            rx.hstack(
                app_badge(
                    song.difficulty,
                    variant="difficulty",
                    size="3",
                ),
                app_badge(
                    song.tuning,
                    size="3",
                ),
                spacing=SMALL_GAP,
            ),
            badge_group(
                song.techniques,
                size="3",
            ),
            secondary_text(
                (
                    "Lección enfocada en dinámica, "
                    "control expresivo, vibrato "
                    "y musicalidad moderna."
                ),
                size="5",
                max_width="800px",
            ),
            spacing=LARGE_GAP,
        ),
        spacing=PAGE_GAP,
    )