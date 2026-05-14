import reflex as rx
from sonablues.components.layouts import base_layout
from sonablues.styles.tokens import (
    INSTRUMENT_CARD_MIN_HEIGHT,
    CARD_PADDING_LARGE,
    )
from sonablues.components.ui.card_link import (
    card_link,
)
from sonablues.styles.spacing import (
    SMALL_GAP,
    SECTION_GAP,
)
from sonablues.components.ui.surface import (
    surface,
)
from sonablues.components.ui.responsive_grid import (
    responsive_grid,
)
from sonablues.components.ui.stacks import (
    stack_start,
    stack_section,
)
from sonablues.components.ui.text import (
    title_text,
    secondary_text,
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
                    size="6",
                ),

                secondary_text(
                    description,
                ),

                spacing=SMALL_GAP,
            ),

            padding=CARD_PADDING_LARGE,

            min_height=INSTRUMENT_CARD_MIN_HEIGHT,

            hoverable=True,
        ),

        href=href,
    )
    
    
def instruments_page() -> rx.Component:

    return base_layout(

        stack_section(

            title_text(
                "Explorar",
                size="9",
            ),

            secondary_text(
                "Selecciona instrumento.",
                size="4",
            ),

            responsive_grid(

                instrument_card(
                    "Guitarra eléctrica",
                    "Blues, rock y fraseo eléctrico.",
                    "/artists/electric",
                ),

                instrument_card(
                    "Guitarra acústica",
                    "Fingerstyle y dinámica acústica.",
                    "/artists/acoustic",
                ),

                columns={
                    "base": "1",
                    "md": "2",
                },
            ),

            spacing=SECTION_GAP,
        )
    )