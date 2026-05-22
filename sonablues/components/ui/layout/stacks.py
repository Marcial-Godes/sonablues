import reflex as rx

from sonablues.styles.tokens import (
    CONTENT_GAP,
    SECTION_GAP,
)


def stack_start(
    *children,
    spacing=CONTENT_GAP,
    align: str = "start",
    width: str = "100%",
    **props,
) -> rx.Component:
    return rx.vstack(
        *children,
        spacing=spacing,
        align=align,
        width=width,
        **props,
    )


def content_stack(
    *children,
    spacing=SECTION_GAP,
    align: str = "stretch",
    width: str = "100%",
    **props,
) -> rx.Component:
    return rx.vstack(
        *children,
        spacing=spacing,
        align=align,
        width=width,
        **props,
    )