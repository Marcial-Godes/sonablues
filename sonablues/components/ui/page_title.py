import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
)


def page_title(
    text: str,
) -> rx.Component:

    return rx.heading(
        text,
        size="9",
        color=TEXT_COLOR,
    )