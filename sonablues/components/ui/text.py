import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    MUTED_TEXT,
)


def title_text(
    text: str,
    **props,
) -> rx.Component:

    return rx.heading(

        text,

        color=TEXT_COLOR,

        **props,
    )


def body_text(
    text: str,
    **props,
) -> rx.Component:

    return rx.text(

        text,

        color=TEXT_COLOR,

        **props,
    )


def secondary_text(
    text: str,
    **props,
) -> rx.Component:

    return rx.text(

        text,

        color=MUTED_TEXT,

        **props,
    )