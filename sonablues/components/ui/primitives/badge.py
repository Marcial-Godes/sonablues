import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    BORDER_COLOR,
    ACCENT_BACKGROUND,
)


def tag_badge(
    text: str,
    size: str = "2",
) -> rx.Component:
    return rx.badge(
        text,
        size=size,
        color=TEXT_COLOR,
        background_color=ACCENT_BACKGROUND,
        border=f"1px solid {BORDER_COLOR}",
        padding_x="0.5rem",
        padding_y="0.15rem",
    )


def badge(
    text: str,
    size: str = "2",
) -> rx.Component:
    return rx.badge(
        text,
        size=size,
    )