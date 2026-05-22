import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.ui.text import (
    secondary_text,
    page_title,
)

from sonablues.components.ui.primitives.badge import badge
from sonablues.components.ui.media.cover_image import cover_image

from sonablues.components.song.difficulty_badge import (
    difficulty_badge,
)
from sonablues.components.ui.primitives import (
    badge_group,
)
from sonablues.components.ui.layout import (
    content_stack,
    stack_start,
)
from sonablues.styles.tokens import (
    BADGE_SIZE_DEFAULT,
    TEXT_SIZE_BODY,
    INLINE_GAP,
    CONTENT_GAP,
    SECTION_TEXT_WIDTH,
)


def song_hero(
    song: Song,
) -> rx.Component:
    return content_stack(
        cover_image(
            src=song.image,
            height="240px",
        ),

        stack_start(
            page_title(
                song.title,
            ),

            rx.hstack(
                difficulty_badge(
                    song.difficulty,
                    size=BADGE_SIZE_DEFAULT,
                ),

                badge(
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