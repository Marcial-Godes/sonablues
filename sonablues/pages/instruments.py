import reflex as rx

from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.layout import (
    page_container,
)

from sonablues.components.cards import (
    instrument_card,
)

from sonablues.components.ui import (
    responsive_grid,
    stack_section,
    title_text,
    secondary_text,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
    SECTION_GAP,
)


def instruments_page() -> rx.Component:
    return base_layout(
        page_container(
            stack_section(
                title_text(
                    "Explorar",
                    size=TITLE_SIZE_PAGE,
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
    )