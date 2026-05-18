import reflex as rx
from sonablues.components.base_layout import (
    base_layout,
)
from sonablues.states.auth_state import AuthState
from sonablues.styles.tokens import (
    CONTENT_GAP,
)



def register_page() -> rx.Component:
    return base_layout(
        rx.vstack(
            rx.heading(
                "Registro",
                size="7",
            ),
            rx.input(
                placeholder="Usuario",
                on_change=AuthState.set_username,
            ),
            rx.input(
                placeholder="Contraseña",
                type="password",
                on_change=AuthState.set_password,
            ),
            rx.button(
                "Crear cuenta",
                on_click=AuthState.register,
            ),
            rx.text(
                AuthState.error_message,
                color="red",
            ),
            spacing=CONTENT_GAP,
            align="start",
        ),
    )