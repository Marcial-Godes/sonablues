import reflex as rx

from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    MUTED_TEXT,
)

from sonablues.styles.spacing import (
    MEDIUM_GAP,
)


def footer() -> rx.Component:

    return rx.hstack(

        rx.vstack(

            rx.text(
                "Sonablues",
                color=TEXT_COLOR,
                weight="bold",
            ),

            rx.text(
                "Modern blues guitar platform",
                color=MUTED_TEXT,
                size="2",
            ),

            spacing="1",
            align="start",
        ),

        rx.spacer(),

        rx.text(
            "Made by Marcial",
            color=MUTED_TEXT,
            size="2",
        ),

        width="100%",

        padding="1.5rem 2rem",

        background_color=CARD_COLOR,

        border_top=f"1px solid {BORDER_COLOR}",

        align="center",
    )