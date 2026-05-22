import reflex as rx

from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)

from sonablues.components.ui.sections import (
    section_card,
    section_header,
)

from sonablues.components.ui.layout import (
    content_stack,
)


def planned_content() -> rx.Component:
    return content_stack(
        section_header(
            PLANNED_CONTENT_TITLE,
            "Contenido adicional planeado para cada lección.",
        ),

        section_card(
            "01",
            "Contenido incluido",

            rx.unordered_list(
                rx.list_item("Tabs sincronizadas"),
                rx.list_item("Vídeo paso a paso"),
                rx.list_item("Backing track"),
                rx.list_item("Loop de práctica"),
                rx.list_item("Sección técnica detallada"),
                spacing="2",
                padding_left="1.25rem",
            ),
        ),
    )