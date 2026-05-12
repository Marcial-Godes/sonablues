import reflex as rx

from sonablues.states.auth_state import AuthState

from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    ACCENT_COLOR,
)


def navbar() -> rx.Component:

    return rx.hstack(

        rx.link(

            rx.heading(
                "Sonablues",
                size="6",
                color=TEXT_COLOR,
            ),

            href="/",
            text_decoration="none",
        ),

        rx.spacer(),

        rx.cond(

            AuthState.is_authenticated,

            rx.hstack(

                rx.hstack(

                    rx.text(
                        "Hola",
                        color=TEXT_COLOR,
                    ),

                    rx.text(
                        AuthState.current_user,
                        color=TEXT_COLOR,
                        weight="bold",
                    ),

                    spacing="2",
                ),
                rx.link(
                    "Favorites",
                    href="/favorites",
                ),

                rx.button(
                    "Logout",
                    on_click=AuthState.logout,
                    background_color=ACCENT_COLOR,
                ),
            ),

            rx.hstack(

                rx.link(
                    "Login",
                    href="/login",
                    color=TEXT_COLOR,
                ),

                rx.link(
                    "Registro",
                    href="/register",
                    color=TEXT_COLOR,
                ),
            ),
        ),

        width="100%",

        padding="1rem 2rem",

        background_color=CARD_COLOR,

        border_bottom=f"1px solid {BORDER_COLOR}",
    )