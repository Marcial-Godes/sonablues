import reflex as rx
from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)
from sonablues.components.ui import (
    content_section,
    content_card,
    stack_start,
    section_row,
)
from sonablues.styles.tokens import (
    CONTENT_GAP
)


def planned_content() -> rx.Component:
    return content_section(
        PLANNED_CONTENT_TITLE,
        "Contenido adicional planeado para cada lección.",

        content_card(
            stack_start(
                section_row(
                    badge="01",
                    title="Contenido incluido",
                ),

                rx.unordered_list(
                    rx.list_item("Tabs sincronizadas"),
                    rx.list_item("Vídeo paso a paso"),
                    rx.list_item("Backing track"),
                    rx.list_item("Loop de práctica"),
                    rx.list_item("Sección técnica detallada"),

                    spacing="3",
                    padding_left="1.25rem",
                ),

                spacing=CONTENT_GAP,
                width="100%",
            ),
        ),
    )