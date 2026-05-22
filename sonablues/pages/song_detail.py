import reflex as rx
from sonablues.constants import (
    SONG_NOT_FOUND,
)
from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.protected_page import (
    protected_page,
)

from sonablues.components.layout import (
    content_container,
)
from sonablues.components.song import (
    practice_tips_section,
    song_hero,
    song_content,
)
from sonablues.components.ui.feedback import (
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

    return protected_page(
        base_layout(
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
    )