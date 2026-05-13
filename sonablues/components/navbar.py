# navbar.py

import reflex as rx

from sonablues.states.auth_state import AuthState

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

from sonablues.styles.spacing import MEDIUM_GAP


def nav_link(text, href, active):

    return rx.link(

        rx.text(
            text,

            color=rx.cond(active, ACCENT_COLOR, TEXT_COLOR),

            weight="medium",

            white_space="nowrap",

            transition="0.2s ease",

            _hover={
                "color": ACCENT_COLOR,
            },
        ),

        href=href,

        text_decoration="none",
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

    desktop_navigation = rx.hstack(

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

        spacing=MEDIUM_GAP,

        align="center",
    )

    desktop_user = rx.hstack(

        rx.text(
            "Hola",
            color=TEXT_COLOR,
        ),

        rx.text(
            AuthState.current_user,

            color=TEXT_COLOR,

            weight="bold",
        ),

        rx.button(
            "Logout",

            on_click=AuthState.logout,

            background_color=ACCENT_COLOR,

            size="2",

            cursor="pointer",
        ),

        spacing="3",

        align="center",
    )

    mobile_menu = rx.drawer.root(

        rx.drawer.trigger(

            rx.icon_button(

                rx.icon("menu"),

                variant="ghost",

                color=TEXT_COLOR,
            ),
        ),

        rx.drawer.overlay(),

        rx.drawer.content(

            rx.vstack(

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

                spacing="6",

                align="start",

                width="100%",

                padding="2rem",
            ),

            background_color=CARD_COLOR,
        ),

        direction="right",
    )

    return rx.hstack(

        rx.link(

            rx.heading(
                "Sonablues",

                size={
                    "base": "5",
                    "md": "6",
                },

                color=TEXT_COLOR,

                white_space="nowrap",
            ),

            href=HOME_ROUTE,

            text_decoration="none",
        ),

        rx.spacer(),

        rx.desktop_only(

            rx.hstack(

                desktop_navigation,

                desktop_user,

                spacing="6",

                align="center",
            ),
        ),

        rx.mobile_and_tablet(

            mobile_menu,
        ),

        width="100%",

        padding={
            "base": "0.8rem 1rem",
            "md": "1rem 1.5rem",
            "lg": "1rem 2rem",
        },

        align="center",

        background_color=CARD_COLOR,

        border_bottom=f"1px solid {BORDER_COLOR}",
    )