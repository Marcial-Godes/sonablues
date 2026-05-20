import reflex as rx
from sonablues.constants import (
    SONG_NOT_FOUND,
)
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.components.layout import (
    content_container,
)
from sonablues.components.song import (
    song_content,
)
from sonablues.components.song.sections import (
    practice_tips_section,
    song_hero,
)
from sonablues.components.ui import (
    empty_state,
)
from sonablues.services import (
    get_song,
)
from sonablues.styles.tokens import (
    PAGE_GAP,
)


def song_detail_page(
    song_slug: str,
) -> rx.Component:
    song = get_song(song_slug)
    if not song:
        return base_layout(
            empty_state(
                title=SONG_NOT_FOUND,
                description=(
                    "The requested lesson does not exist "
                    "or is currently unavailable."
                ),
            )
        )

    return base_layout(
        content_container(
            rx.vstack(
                song_hero(song),
                song_content(song),
                practice_tips_section(),
                width="100%",
                spacing=PAGE_GAP,
                align="start",
            ),
        )
    )