import reflex as rx

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.cards.song_card import (
    song_card,
)

from sonablues.components.ui import (
    section_title,
    empty_state,
)

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.utils.protected import (
    protected_page,
)

from sonablues.styles.spacing import (
    LARGE_GAP,
)

from sonablues.states.profile_state import (
    ProfileState,
)


def profile_content() -> rx.Component:
    return rx.vstack(

        rx.heading(
            "Perfil",
            size="8",
        ),

        rx.text(
            f"Usuario actual: {AuthState.current_user}",
            size="4",
        ),

        rx.vstack(

            section_title(
                "Favorite songs",
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
                    },

                    spacing=LARGE_GAP,
                    width="100%",
                ),

                empty_state(
                    title="No favorite songs yet",
                ),
            ),

            spacing=LARGE_GAP,
            width="100%",
        ),

        spacing=LARGE_GAP,
        align="start",
        width="100%",
    )


def profile_page() -> rx.Component:
    return base_layout(

        protected_page(
            profile_content()
        )
    )