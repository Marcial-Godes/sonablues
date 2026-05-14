import reflex as rx

from sonablues.styles.spacing import (
    EXTRA_SMALL_GAP,
)

from sonablues.styles.theme import (
    BORDER_COLOR,
    TEXT_COLOR,
    ACCENT_BACKGROUND,
)


def badge_group(
    items,
    size: str = "2",
) -> rx.Component:

    return rx.flex(

        rx.foreach(

            items,

            lambda item: rx.badge(

                item,

                size=size,

                color=TEXT_COLOR,

                background_color=ACCENT_BACKGROUND,

                border=f"1px solid {BORDER_COLOR}",

                padding_x="0.5rem",

                padding_y="0.15rem",
            ),
        ),

        wrap="wrap",

        gap=EXTRA_SMALL_GAP,

        width="100%",
    )