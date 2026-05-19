import reflex as rx

from sonablues.styles.tokens import (
    CONTENT_GAP,
    SECTION_GAP,
)


def stack_start(
    *children,
    spacing=CONTENT_GAP,
    **props,
) -> rx.Component:
    return rx.vstack(
        *children,
        spacing=spacing,
        align=props.pop("align", "start"),
        width=props.pop("width", "100%"),
        **props,
    )


def content_stack(
    *children,
    spacing=SECTION_GAP,
    **props,
) -> rx.Component:
    return rx.vstack(
        *children,
        spacing=spacing,
        align=props.pop("align", "stretch"),
        width=props.pop("width", "100%"),
        **props,
    )