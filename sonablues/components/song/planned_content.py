import reflex as rx
from sonablues.constants import (
    PLANNED_CONTENT_TITLE,
)
from sonablues.components.ui import (
    surface,
    content_section,
    stack_start,
    body_text,
)
from sonablues.styles.tokens import (
    CARD_PADDING,
    CONTENT_GAP
)


def planned_content() -> rx.Component:
    return content_section(
        PLANNED_CONTENT_TITLE,
        "Contenido adicional planeado para cada lección.",
        surface(
            stack_start(
                body_text("• Tabs sincronizadas"),
                body_text("• Vídeo paso a paso"),
                body_text("• Backing track"),
                body_text("• Loop de práctica"),
                body_text("• Sección técnica detallada"),
                spacing=CONTENT_GAP,
            ),
            width="100%",
            padding=CARD_PADDING,
            min_height="unset",
        ),
    )
    