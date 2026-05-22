import reflex as rx

from ..layout import (
    stack_start,
)

from ..text import (
    section_label,
)

from sonablues.components.ui.cards import (
    content_card,
)

from sonablues.styles.theme import (
    ACCENT_COLOR,
    ACCENT_BACKGROUND,
    BADGE_TEXT_COLOR,
)

from sonablues.styles.tokens import (
    BADGE_SIZE_SMALL,
    COMPACT_STACK_SPACING,
    TEXT_BLOCK_SPACING,
    TEXT_INLINE_PADDING,
    CONTENT_GAP,
)

from sonablues.styles.radius import (
    BADGE_RADIUS,
)


def section_card_header(
    badge: str,
    title: str,
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
    )


def section_card(
    badge: str,
    title: str,
    *children,
    spacing: str = CONTENT_GAP,
    **props,
) -> rx.Component:
    return content_card(
        stack_start(
            section_card_header(
                badge,
                title,
            ),

            *children,

            spacing=spacing,
        ),
        **props,
    )