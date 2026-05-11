import reflex as rx

from sonablues.styles.theme import (
    MUTED_TEXT,
)


def muted_text(
    text: str,
    size: str = "4",
    **props,
) -> rx.Component:

    return rx.text(
        text,
        color=MUTED_TEXT,
        size=size,
        line_height="1.7",

        **props,
    )