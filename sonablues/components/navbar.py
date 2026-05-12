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
    
    current_path = rx.State.router.page.path
    is_home = rx.cond(
        current_path == PROFILE_ROUTE,
        False,
        rx.cond(
            current_path == FAVORITES_ROUTE,
            False,
            True,
        ),
    )
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
                _hover={
                "color": ACCENT_COLOR,
                },
            ),
            rx.hstack(
                rx.link(
                    rx.text(
                        "Home",
                        color=rx.cond(
                        is_home,
                        ACCENT_COLOR,
                        TEXT_COLOR,
                    ),
                        weight="medium",
                        transition="0.2s ease",
                        _hover={
                            "color": ACCENT_COLOR,
                        },
                    ),
                    href=HOME_ROUTE,
                    text_decoration="none",
                ),

                rx.cond(
                    AuthState.is_authenticated,
                    rx.fragment(
                        rx.link(
                            rx.text(
                                "Profile",
                                color=rx.cond(
                                    current_path == PROFILE_ROUTE,
                                    ACCENT_COLOR,
                                    TEXT_COLOR,
                                ),
                                weight="medium",
                                transition="0.2s ease",
                                _hover={
                                    "color": ACCENT_COLOR,
                                },
                            ),
                            href=PROFILE_ROUTE,
                            text_decoration="none",
                        ),

                        rx.link(
                            rx.text(
                                "Favorites",
                                color=rx.cond(
                                    current_path == FAVORITES_ROUTE,
                                    ACCENT_COLOR,
                                    TEXT_COLOR,
                                ),
                                weight="medium",
                                transition="0.2s ease",
                                _hover={
                                    "color": ACCENT_COLOR,
                                },
                            ),
                            href=FAVORITES_ROUTE,
                            text_decoration="none",
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