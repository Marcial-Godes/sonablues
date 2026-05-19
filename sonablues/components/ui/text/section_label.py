import reflex as rx

from sonablues.styles.theme import (
    SECTION_LABEL_COLOR,
)
from sonablues.styles.tokens import (
    FONT_WEIGHT_MEDIUM,
    LETTER_SPACING_TIGHT,
    LINE_HEIGHT_COMPACT,
)


def section_label(
    text: str,
    **props,
) -> rx.Component:
    return rx.text(
        text,
        font_weight=FONT_WEIGHT_MEDIUM,
        letter_spacing=LETTER_SPACING_TIGHT,
        line_height=LINE_HEIGHT_COMPACT,
        color=SECTION_LABEL_COLOR,
        **props,
    )