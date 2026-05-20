import reflex as rx
from ..text import (
    section_label,
)
from sonablues.styles.theme import (
    ACCENT_COLOR,
    ACCENT_BACKGROUND,
    BADGE_TEXT_COLOR,
)
from sonablues.styles.tokens import (
    BADGE_RADIUS,
    BADGE_SIZE_SMALL,
    COMPACT_STACK_SPACING,
    TEXT_BLOCK_SPACING,
    TEXT_INLINE_PADDING,
)


def section_row(
    badge: str,
    title: str,
    **props,
) -> rx.Component:
    return rx.hstack(
        rx.badge(
            badge,
            radius=BADGE_RADIUS,
            size=BADGE_SIZE_SMALL,
            color=BADGE_TEXT_COLOR,
            background=ACCENT_BACKGROUND,
            border=f"1px solid {ACCENT_COLOR}08",
        ),
        section_label(
            title,
        ),
        spacing=COMPACT_STACK_SPACING,
        align="center",
        width="100%",
        padding_x=TEXT_INLINE_PADDING,
        padding_top=TEXT_BLOCK_SPACING,
        **props,
    )