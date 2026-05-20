import reflex as rx

from sonablues.components.ui import (
    card_link,
    surface,
    title_text,
    secondary_text,
)
from sonablues.components.ui.layout import (
    stack_start,
)

from sonablues.styles.tokens import (
    INSTRUMENT_CARD_MIN_HEIGHT,
    CARD_PADDING,
    TITLE_SIZE_SECTION,
    CONTENT_GAP,
)


def instrument_card(
    title: str,
    description: str,
    href: str,
) -> rx.Component:
    return card_link(
        surface(
            stack_start(
                title_text(
                    title,
                    size=TITLE_SIZE_SECTION,
                ),

                secondary_text(
                    description,
                ),

                spacing=CONTENT_GAP,
            ),

            padding=CARD_PADDING,
            min_height=INSTRUMENT_CARD_MIN_HEIGHT,
            hoverable=True,
        ),

        href=href,
    )