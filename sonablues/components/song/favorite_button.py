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

from sonablues.styles.tokens import (
    INPUT_ICON_SIZE,
)


def favorite_button(
    song_slug: str,
    compact: bool = False,
) -> rx.Component:

    is_favorite = (
        AuthState.favorite_songs_list.contains(
            song_slug,
        )
    )

    icon = rx.cond(
        is_favorite,

        rx.image(
            src="/icons/heart-filled.svg",
            width=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),

            height=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),
        ),

        rx.image(
            src="/icons/heart-outline.svg",
            width=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),

            height=rx.cond(
                compact,
                "18px",
                INPUT_ICON_SIZE,
            ),
        ),
    )

    return rx.button(
        rx.cond(
            compact,

            icon,

            rx.hstack(
                icon,

                rx.cond(
                    is_favorite,
                    "Favorited",
                    "Save",
                ),

                spacing="2",
                align="center",
            ),
        ),

        on_click=lambda: AuthState.toggle_favorite(
            song_slug,
        ),

        background_color=rx.cond(
            is_favorite,
            ACCENT_BACKGROUND,
            "rgba(0,0,0,0.48)" if compact else "transparent",
        ),

        color=rx.cond(
            is_favorite,
            ACCENT_COLOR,
            TEXT_COLOR,
        ),

        border=rx.cond(
            compact,
            "1px solid rgba(255,255,255,0.08)",

            rx.cond(
                is_favorite,
                f"1px solid {ACCENT_COLOR}",
                f"1px solid {BORDER_COLOR}",
            ),
        ),

        backdrop_filter=rx.cond(
            compact,
            "blur(10px)",
            "none",
        ),

        _hover={
            "border": f"1px solid {ACCENT_COLOR}",
            "color": ACCENT_COLOR,
            "background_color": ACCENT_BACKGROUND,
        },

        transition="all 0.2s ease",
        cursor="pointer",

        border_radius=rx.cond(
            compact,
            "9999px",
            "0.5rem",
        ),

        min_width=rx.cond(
            compact,
            "40px",
            "auto",
        ),

        width=rx.cond(
            compact,
            "40px",
            "auto",
        ),

        height=rx.cond(
            compact,
            "40px",
            "auto",
        ),

        padding=rx.cond(
            compact,
            "0",
            "0.35rem 0.75rem 0.35rem 0.75rem",
        ),

        display="flex",
        align_items="center",
        justify_content="center",

        size="2",
    )