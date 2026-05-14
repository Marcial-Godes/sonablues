from sonablues.components.ui.text import (
    title_text,
)
from sonablues.styles.tokens import (
    TITLE_SIZE_SECTION,
)


def section_title(
    text: str,
):
    return title_text(
        text,
        size=TITLE_SIZE_SECTION,
    )