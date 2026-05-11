import reflex as rx

from sonablues.data.models.song_model import Song

from sonablues.components.ui import (
    page_title,
    muted_text,
    badge_group,
    cover_image,
    meta_badge,
)

from sonablues.styles.sizes import (
    CONTENT_WIDTH,
)

from sonablues.styles.spacing import (
    SMALL_GAP,
    LARGE_GAP,
    PAGE_GAP,
)


def song_hero(song: Song) -> rx.Component:

    return rx.vstack(

        cover_image(
            src=song.image,
            height="460px",
            max_width=CONTENT_WIDTH,
        ),

        rx.vstack(

            page_title(
                song.title,
            ),

            rx.hstack(

                meta_badge(
                    song.difficulty,
                    color_scheme="blue",
                    size="3",
                ),

                meta_badge(
                    song.tuning,
                    size="3",
                ),

                spacing=SMALL_GAP,
            ),

            badge_group(
                song.techniques,
                size="3",
            ),

            muted_text(
                (
                    "Lección enfocada en dinámica, "
                    "control expresivo, vibrato "
                    "y musicalidad moderna."
                ),
                size="5",
                max_width="800px",
            ),

            spacing=LARGE_GAP,
            align="start",
            width="100%",
        ),

        spacing=PAGE_GAP,
        align="start",
        width="100%",
    )