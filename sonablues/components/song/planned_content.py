import reflex as rx

from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)

from sonablues.components.ui import (
    content_section,
    section_card,
    content_list,
)


def planned_content() -> rx.Component:
    return content_section(
        PLANNED_CONTENT_TITLE,
        "Contenido adicional planeado para cada lección.",

        section_card(
            "01",
            "Contenido incluido",

            content_list(
                rx.list_item("Tabs sincronizadas"),
                rx.list_item("Vídeo paso a paso"),
                rx.list_item("Backing track"),
                rx.list_item("Loop de práctica"),
                rx.list_item("Sección técnica detallada"),
            ),
        ),
    )