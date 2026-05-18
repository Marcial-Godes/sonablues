import reflex as rx
from sonablues.styles.theme import (
    CARD_COLOR,
    BORDER_COLOR,
)
from sonablues.components.ui import (
    label_text,
    caption_text,
    stack_start,
)
from sonablues.styles.tokens import (
    INLINE_GAP,
    CONTENT_GAP,
    FOOTER_PADDING_Y,
    FOOTER_PADDING_X,
)


def footer() -> rx.Component:
    return rx.flex(
        stack_start(
            label_text(
            "Sonablues",
        ),
            caption_text(
                "Modern blues guitar platform",
            ),
            spacing=INLINE_GAP,
        ),
        rx.spacer(),
        caption_text(
            "Made by Marcial",
        ),
        direction={
            "base": "column",
            "sm": "row",
        },
        gap=CONTENT_GAP,
        align={
            "base": "start",
            "sm": "center",
        },
        width="100%",
        padding_y=FOOTER_PADDING_Y,
        padding_x=FOOTER_PADDING_X,
        background_color=CARD_COLOR,
        border_top=f"1px solid {BORDER_COLOR}",
    )