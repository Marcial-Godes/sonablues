import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.protected_page import (
    protected_page,
)

from sonablues.components.layout import (
    page_container,
)
from sonablues.components.song import (
    song_card,
)
from sonablues.states.profile_state import (
    ProfileState,
)

from sonablues.components.ui.text import (
    page_title,
)
from sonablues.components.ui.feedback import (
    empty_state,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)


def favorites_content() -> rx.Component:

    return page_container(
        content_stack(
            page_title(
                "Favorite Songs",
            ),

            rx.cond(
                ProfileState.favorite_songs.length() > 0,

                responsive_grid(
                    rx.foreach(
                        ProfileState.favorite_songs,
                        lambda song: song_card(song),
                    ),
                ),

                empty_state(
                    title="No favorite songs yet",
                    description=(
                        "Start adding songs to your favorites."
                    ),
                ),
            ),
        )
    )

def favorites_page() -> rx.Component:

    return protected_page(
        base_layout(
            favorites_content(),
        )
    )