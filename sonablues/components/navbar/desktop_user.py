import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.routes import (
    LOGIN_ROUTE,
)

from sonablues.styles.theme import (
    ACCENT_COLOR,
)

from sonablues.styles.tokens import (
    NAVBAR_GAP,
)

from sonablues.components.ui.text import (
    caption_text,
    label_text,
)


def desktop_user() -> rx.Component:

    return rx.cond(

        AuthState.is_authenticated,

        rx.hstack(
            caption_text(
                "Hola",
            ),

            label_text(
                AuthState.current_user,
            ),

            rx.button(
                "Logout",
                on_click=AuthState.logout,
                background_color=ACCENT_COLOR,
                size="2",
                cursor="pointer",
            ),

            spacing=NAVBAR_GAP,
        ),

        rx.button(
            "Login",
            on_click=rx.redirect(
                LOGIN_ROUTE,
            ),
            background_color=ACCENT_COLOR,
            size="2",
            cursor="pointer",
        ),
    )