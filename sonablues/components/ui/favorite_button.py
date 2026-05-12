import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.styles.theme import (
    ACCENT_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    ACCENT_BACKGROUND,
)


def favorite_button(
    song_slug: str,
) -> rx.Component:

    is_favorite = (
        AuthState.favorite_songs_list.contains(
            song_slug,
        )
    )

    return rx.button(

        rx.hstack(

            rx.cond(

                is_favorite,

                rx.image(
                    src="/icons/heart-filled.svg",
                    width="18px",
                    height="18px",
                ),

                rx.image(
                    src="/icons/heart-outline.svg",
                    width="18px",
                    height="18px",
                ),
            ),

            rx.cond(
                is_favorite,
                "Favorited",
                "Add to favorites",
            ),

            spacing="2",
            align="center",
        ),

        on_click=lambda: AuthState.toggle_favorite(
            song_slug,
        ),

        background_color=rx.cond(
            is_favorite,
            ACCENT_BACKGROUND,
            "transparent",
        ),

        color=rx.cond(
            is_favorite,
            ACCENT_COLOR,
            TEXT_COLOR,
        ),

        border=rx.cond(
            is_favorite,
            f"1px solid {ACCENT_COLOR}",
            f"1px solid {BORDER_COLOR}",
        ),

        _hover={
            "border": f"1px solid {ACCENT_COLOR}",
            "color": ACCENT_COLOR,
            "background_color": ACCENT_BACKGROUND,
        },

        transition="all 0.2s ease",

        cursor="pointer",

        size="3",
    )