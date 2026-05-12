import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.routes import (
    HOME_ROUTE,
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
)

from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    ACCENT_COLOR,
)

from sonablues.styles.spacing import (
    MEDIUM_GAP,
)


def navbar() -> rx.Component:

    nav_link_style = {
        "color": TEXT_COLOR,
        "text_decoration": "none",
        "font_weight": "500",
    }

    return rx.hstack(

        rx.hstack(

            rx.link(

                rx.heading(
                    "Sonablues",
                    size="6",
                    color=TEXT_COLOR,
                ),

                href=HOME_ROUTE,

                text_decoration="none",
            ),

            rx.hstack(

                rx.link(
                    "Home",
                    href=HOME_ROUTE,
                    style=nav_link_style,
                ),

                rx.cond(

                    AuthState.is_authenticated,

                    rx.fragment(

                        rx.link(
                            "Profile",
                            href=PROFILE_ROUTE,
                            style=nav_link_style,
                        ),

                        rx.link(
                            "Favorites",
                            href=FAVORITES_ROUTE,
                            style=nav_link_style,
                        ),
                    ),
                ),

                spacing=MEDIUM_GAP,
                align="center",
            ),

            spacing="8",
            align="center",
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

                rx.button(
                    "Logout",
                    on_click=AuthState.logout,
                    background_color=ACCENT_COLOR,
                    cursor="pointer",
                ),

                spacing=MEDIUM_GAP,
                align="center",
            ),

            rx.hstack(

                rx.link(
                    "Login",
                    href="/login",
                    color=TEXT_COLOR,
                ),

                rx.link(
                    "Register",
                    href="/register",
                    color=TEXT_COLOR,
                ),

                spacing=MEDIUM_GAP,
            ),
        ),

        width="100%",

        padding="1rem 2rem",

        background_color=CARD_COLOR,

        border_bottom=f"1px solid {BORDER_COLOR}",
    )