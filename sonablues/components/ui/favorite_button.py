import reflex as rx
from sonablues.states.auth_state import (
    AuthState,
)
from sonablues.styles.theme import (
    ACCENT_COLOR,
)


def favorite_button(
    song_slug: str,
) -> rx.Component:
    return rx.button(
        rx.cond(
            AuthState.favorite_songs_list.contains(
                song_slug,
            ),
            "❤️ Favorited",
            "🤍 Add to favorites",
        ),
        on_click=lambda: AuthState.toggle_favorite(
            song_slug,
        ),
        background_color=ACCENT_COLOR,
        size="3",
        cursor="pointer",
    )