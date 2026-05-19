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
    BADGE_SIZE_DEFAULT,
    TEXT_SIZE_BODY,
    INLINE_GAP,
    CONTENT_GAP,
    SECTION_TEXT_WIDTH,
)


def song_hero(
    song: Song,
) -> rx.Component:
    return stack_section(
        cover_image(
            src=song.image,
            height="240px",
        ),

        stack_start(
            page_title(
                song.title,
            ),

            rx.hstack(
                app_badge(
                    song.difficulty,
                    variant="difficulty",
                    size=BADGE_SIZE_DEFAULT,
                ),

                app_badge(
                    song.tuning,
                    size=BADGE_SIZE_DEFAULT,
                ),

                spacing=INLINE_GAP,
                wrap="wrap",
            ),

            badge_group(
                song.techniques,
                size=BADGE_SIZE_DEFAULT,
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

        spacing=CONTENT_GAP,
    )