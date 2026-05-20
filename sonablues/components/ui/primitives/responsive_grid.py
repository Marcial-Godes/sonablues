import reflex as rx
from sonablues.styles.tokens import (
    GRID_GAP,
)


def responsive_grid(
    *children,
    columns: dict | None = None,
    **props,
) -> rx.Component:
    default_columns = {
        "base": "1",
        "sm": "2",
        "lg": "3",
        "2xl": "4",
    }
    return rx.grid(
        *children,
        columns=columns or default_columns,
        spacing=GRID_GAP,
        width="100%",
        align_items="stretch",
        auto_rows="1fr",
        **props,
    )