import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
)


def section_title(
    text: str,
) -> rx.Component:

    return rx.heading(
        text,
        size="6",
        color=TEXT_COLOR,
    )