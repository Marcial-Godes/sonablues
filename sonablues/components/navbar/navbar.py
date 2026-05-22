import reflex as rx
from sonablues.routes import (
    PROFILE_ROUTE,
    FAVORITES_ROUTE,
    HOME_ROUTE,
)
from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
)
from sonablues.styles.tokens import (
    NAVBAR_SECTION_GAP,
    NAVBAR_PADDING_X,
    NAVBAR_PADDING_Y,
)
from sonablues.components.ui.text import (
    title_text,
)
from .desktop_navigation import (
    desktop_navigation,
)
from .desktop_user import (
    desktop_user,
)
from .mobile_menu import (
    mobile_menu,
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
        rx.link(
            title_text(
                "Sonablues",
                size={
                    "base": "5",
                    "md": "6",
                },
                white_space="nowrap",
                width="auto",
            ),
            href=HOME_ROUTE,
            text_decoration="none",
        ),
        rx.spacer(),
        rx.desktop_only(
            rx.hstack(
                desktop_navigation(
                    current_path,
                    is_home,
                ),
                desktop_user(),
                spacing=NAVBAR_SECTION_GAP,
            ),
        ),

        rx.mobile_and_tablet(
            mobile_menu(
                current_path,
                is_home,
            ),
        ),
        width="100%",
        padding_x=NAVBAR_PADDING_X,
        padding_y=NAVBAR_PADDING_Y,
        align="center",
        background_color=CARD_COLOR,
        border_bottom=f"1px solid {BORDER_COLOR}",
    )