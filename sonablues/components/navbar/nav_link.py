import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    ACCENT_COLOR,
)

from sonablues.styles.transitions import (
    CARD_TRANSITION,
)

from sonablues.components.ui import (
    label_text,
)


def nav_link(
    text,
    href,
    active,
):
    return rx.link(
        label_text(
            text,
            color=rx.cond(
                active,
                ACCENT_COLOR,
                TEXT_COLOR,
            ),
            weight="medium",
            white_space="nowrap",
            transition=CARD_TRANSITION,
            _hover={
                "color": ACCENT_COLOR,
            },
        ),
        href=href,
        text_decoration="none",
    )