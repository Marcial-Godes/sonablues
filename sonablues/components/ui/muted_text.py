from sonablues.components.ui.text import (
    secondary_text,
)


def muted_text(
    text: str,
    size: str = "4",
    **props,
):
    return secondary_text(
        text,
        size=size,
        line_height="1.7",
        **props,
    )