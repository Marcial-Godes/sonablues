import reflex as rx

from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.styles.tokens import (
    CONTENT_GAP,
)


def register_page() -> rx.Component:

    return base_layout(
        rx.center(
            rx.form(

                rx.vstack(
                    rx.heading(
                        "Registro",
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
                        "Crear cuenta",
                        type="submit",
                        width="100%",
                    ),

                    rx.text(
                        AuthState.error_message,
                        color="red",
                    ),

                    spacing=CONTENT_GAP,
                    align="start",
                    width="100%",
                ),

                on_submit=AuthState.register,
                reset_on_submit=False,
            ),

            width="100%",
            min_height="70vh",
        )
    )