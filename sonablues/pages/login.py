import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.states.auth_state import (
    AuthState,
)
from sonablues.styles.theme import (
    CARD_COLOR,
    ACCENT_COLOR,
)
from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def login_page() -> rx.Component:
    return base_layout(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.heading(
                        "Login",
                        size="7",
                    ),
                    rx.input(
                        placeholder="Usuario",
                        on_change=AuthState.set_username,
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        on_change=AuthState.set_password,
                        width="100%",
                    ),
                    rx.button(
                        "Entrar",
                        on_click=AuthState.login,
                        width="100%",
                        background_color=ACCENT_COLOR,
                    ),
                    rx.text(
                        AuthState.error_message,
                        color="red",
                    ),
                    spacing=CONTENT_GAP,
                    width="100%",
                ),
                background_color=CARD_COLOR,
                padding="2rem",
                border_radius="12px",
                width="400px",
            ),
            width="100%",
            min_height="70vh",
        )
    )