import reflex as rx

from sonablues.styles.theme import (
    ACCENT_COLOR,
)


def app_button(
    text: str,
    href: str | None = None,
    variant: str = "solid",
    **props,
) -> rx.Component:

    button = rx.button(

        text,

        background_color=(
            ACCENT_COLOR
            if variant == "solid"
            else "transparent"
        ),

        variant=(
            "solid"
            if variant == "solid"
            else "outline"
        ),

        size="3",

        cursor="pointer",

        **props,
    )

    if href:

        return rx.link(

            button,

            href=href,

            text_decoration="none",
        )

    return button