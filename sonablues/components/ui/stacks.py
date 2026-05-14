import reflex as rx

from sonablues.styles.spacing import (
    SMALL_GAP,
    MEDIUM_GAP,
)


def stack_start(
    *children,
    spacing: str = SMALL_GAP,
    **props,
) -> rx.Component:

    return rx.vstack(

        *children,

        spacing=spacing,

        align="start",

        width="100%",

        **props,
    )


def stack_section(
    *children,
    spacing: str = MEDIUM_GAP,
    **props,
) -> rx.Component:

    return rx.vstack(

        *children,

        spacing=spacing,

        align="start",

        width="100%",

        **props,
    )