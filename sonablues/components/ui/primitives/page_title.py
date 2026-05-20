from ..text import (
    title_text,
)
from sonablues.styles.tokens import (
    TITLE_SIZE_PAGE,
)


def page_title(
    text: str,
):
    return title_text(
        text,
        size=TITLE_SIZE_PAGE,
    )