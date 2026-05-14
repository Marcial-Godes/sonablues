import reflex as rx

from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
    TEXT_COLOR,
    MUTED_TEXT,
)


def footer() -> rx.Component:

    return rx.flex(

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

        direction={
            "base": "column",
            "sm": "row",
        },

        gap="4",

        align={
            "base": "start",
            "sm": "center",
        },

        width="100%",

        padding={
            "base": "1rem",
            "md": "1.5rem 2rem",
        },

        background_color=CARD_COLOR,

        border_top=f"1px solid {BORDER_COLOR}",
    )