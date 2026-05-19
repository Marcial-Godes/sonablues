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
    TEXT_COLOR,
    ACCENT_COLOR,
)

from sonablues.styles.tokens import (
    NAVBAR_SECTION_GAP,
    NAVBAR_DRAWER_PADDING,
)

from sonablues.components.ui import (
    stack_start,
)

from .nav_link import (
    nav_link,
)


def mobile_menu(
    current_path,
    is_home,
) -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon_button(
                rx.icon("menu"),
                variant="ghost",
                color=TEXT_COLOR,
            ),
        ),

        rx.drawer.overlay(),

        rx.drawer.content(
            stack_start(
                nav_link(
                    "Home",
                    HOME_ROUTE,
                    is_home,
                ),

                rx.cond(
                    AuthState.is_authenticated,
                    rx.fragment(
                        nav_link(
                            "Profile",
                            PROFILE_ROUTE,
                            current_path == PROFILE_ROUTE,
                        ),

                        nav_link(
                            "Favorites",
                            FAVORITES_ROUTE,
                            current_path == FAVORITES_ROUTE,
                        ),

                        rx.button(
                            "Logout",
                            on_click=AuthState.logout,
                            background_color=ACCENT_COLOR,
                            width="100%",
                        ),
                    ),
                ),
                spacing=NAVBAR_SECTION_GAP,
                padding=NAVBAR_DRAWER_PADDING,
            ),
            background_color=CARD_COLOR,
        ),
        direction="right",
    )