import reflex as rx

from sonablues.styles.theme import (
    ACCENT_COLOR,
)


def app_button(
    text: str,
    href: str | None = None,
    variant: str = "solid",
    size: str = "3",
    **props,
) -> rx.Component:

    button = rx.button(
        text,
        background_color=(
            ACCENT_COLOR
            if variant == "solid"
            else "transparent"
        ),
        variant=variant,
        size=size,
        cursor="pointer",
        **props,
    )

    if not href:
        return button

    return rx.link(
        button,
        href=href,
        text_decoration="none",
    )