import reflex as rx
from sonablues.data.models.song_model import Song
from sonablues.components.layout.content_container import (
    content_container,
)
from sonablues.components.song import (
    song_video_section,
    planned_content,
)
from sonablues.components.ui import (
    favorite_button,
    stack_section,
)
from sonablues.styles.tokens import (
    PAGE_GAP,
)


def song_content(song: Song) -> rx.Component:
    return stack_section(
        favorite_button(
            song.slug,
        ),
        content_container(
            stack_section(
                song_video_section(song),
                planned_content(),
            )
        ),
        spacing=PAGE_GAP,
    )