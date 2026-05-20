import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    BORDER_COLOR,
    ACCENT_BACKGROUND,
)


def app_badge(
    text: str,
    variant: str = "default",
    size: str = "2",
) -> rx.Component:

    if variant == "difficulty":

        color_scheme = rx.cond(
            text == "Beginner",
            "green",

            rx.cond(
                text == "Intermediate",
                "orange",
                "red",
            ),
        )

        return rx.badge(
            text,
            size=size,
            color_scheme=color_scheme,
            variant="soft",
        )

    if variant == "tag":

        return rx.badge(
            text,

            size=size,

            color=TEXT_COLOR,

            background_color=ACCENT_BACKGROUND,

            border=f"1px solid {BORDER_COLOR}",

            padding_x="0.5rem",

            padding_y="0.15rem",
        )

    return rx.badge(
        text,
        size=size,
    )