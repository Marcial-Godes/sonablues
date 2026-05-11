import reflex as rx

from sonablues.styles.theme import (
    ACCENT_COLOR,
)


def action_button(
    text: str,
    **props,
) -> rx.Component:

    return rx.button(

        text,

        background_color=ACCENT_COLOR,

        size="3",

        cursor="pointer",

        **props,
    )