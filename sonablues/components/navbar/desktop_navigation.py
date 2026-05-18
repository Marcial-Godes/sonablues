import reflex as rx

from sonablues.states.auth_state import (
    AuthState,
)

from sonablues.routes import (
    HOME_ROUTE,
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
)

from sonablues.styles.tokens import (
    NAVBAR_GAP,
)

from .nav_link import (
    nav_link,
)


def desktop_navigation(
    current_path,
    is_home,
) -> rx.Component:
    return rx.hstack(
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
            ),
        ),

        spacing=NAVBAR_GAP,
    )