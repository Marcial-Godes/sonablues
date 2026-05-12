import reflex as rx

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.cards.song_card import (
    song_card,
)

from sonablues.components.ui import (
    page_title,
    empty_state,
)

from sonablues.states.profile_state import (
    ProfileState,
)

from sonablues.utils.protected import (
    protected_page,
)

from sonablues.styles.spacing import (
    LARGE_GAP,
)


def favorites_content() -> rx.Component:

    return rx.vstack(

        page_title(
            "Favorite Songs",
        ),

        rx.cond(

            ProfileState.favorite_songs.length() > 0,

            rx.grid(

                rx.foreach(

                    ProfileState.favorite_songs,

                    lambda song: song_card(song),
                ),

                columns={
                    "base": "1",
                    "md": "2",
                    "lg": "3",
                },

                spacing=LARGE_GAP,
                width="100%",
            ),

            empty_state(
                title="No favorite songs yet",
                description=(
                    "Start adding songs to your favorites."
                ),
            ),
        ),

        spacing=LARGE_GAP,
        align="start",
        width="100%",
    )


def favorites_page() -> rx.Component:

    return base_layout(

        protected_page(
            favorites_content(),
        )
    )