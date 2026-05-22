import reflex as rx

from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.protected_page import (
    protected_page,
)

from sonablues.components.instrument.ui import (
    instrument_card,
)

from sonablues.components.layout import (
    page_container,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)

from sonablues.components.ui.text import (
    secondary_text,
    title_text,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
)


def instruments_page() -> rx.Component:
    return protected_page(
        base_layout(
            page_container(
                content_stack(
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
                )
            )
        )
    )