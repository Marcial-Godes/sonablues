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
from sonablues.styles.tokens import (
    SONG_HERO_IMAGE_HEIGHT,
    SECTION_TEXT_WIDTH,
    BADGE_SIZE,
    TEXT_SIZE_BODY,
    INLINE_GAP,
    CONTENT_GAP,
    SECTION_GAP,
)


def song_hero(
    song: Song,
) -> rx.Component:
    return stack_section(
        cover_image(
            src=song.image,
            height=SONG_HERO_IMAGE_HEIGHT,
        ),
        stack_start(
            page_title(
                song.title,
            ),
            rx.hstack(
                app_badge(
                    song.difficulty,
                    variant="difficulty",
                    size=BADGE_SIZE,
                ),
                app_badge(
                    song.tuning,
                    size=BADGE_SIZE,
                ),
                spacing=INLINE_GAP,
            ),
            badge_group(
                song.techniques,
                size=BADGE_SIZE,
            ),
            secondary_text(
                (
                    "Lección enfocada en dinámica, "
                    "control expresivo, vibrato "
                    "y musicalidad moderna."
                ),
                size=TEXT_SIZE_BODY,
                max_width=SECTION_TEXT_WIDTH,
            ),
            spacing=CONTENT_GAP,
        ),
        spacing=SECTION_GAP,
    )