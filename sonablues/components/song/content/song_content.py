import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.song.sections import (
    planned_content,
    song_video_section,
)
from sonablues.components.song import (
    favorite_button,
)
from sonablues.components.ui.layout import (
    content_stack,
)


def song_content(song: Song) -> rx.Component:
    return content_stack(
        favorite_button(
            song.slug,
        ),
        song_video_section(song),
        planned_content(),
    )