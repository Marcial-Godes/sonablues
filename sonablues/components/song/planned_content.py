import reflex as rx

from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)

from sonablues.components.ui import (
    content_section,
    section_card,
)

from sonablues.styles.tokens import (
    LIST_SPACING,
    LIST_PADDING_LEFT,
)


def planned_content() -> rx.Component:
    return content_section(
        PLANNED_CONTENT_TITLE,
        "Contenido adicional planeado para cada lección.",

        section_card(
            "01",
            "Contenido incluido",

            rx.unordered_list(
                rx.list_item("Tabs sincronizadas"),
                rx.list_item("Vídeo paso a paso"),
                rx.list_item("Backing track"),
                rx.list_item("Loop de práctica"),
                rx.list_item("Sección técnica detallada"),

                spacing=LIST_SPACING,
                padding_left=LIST_PADDING_LEFT,
            ),
        ),
    )