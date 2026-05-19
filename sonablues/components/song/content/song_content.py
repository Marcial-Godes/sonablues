import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.song import (
    song_video_section,
    planned_content,
)
from sonablues.components.ui import (
    favorite_button,
    content_stack,
)
from sonablues.styles.tokens import (
    PAGE_GAP,
)


def song_content(song: Song) -> rx.Component:
    return content_stack(
        favorite_button(
            song.slug,
        ),
        song_video_section(song),
        planned_content(),
    )