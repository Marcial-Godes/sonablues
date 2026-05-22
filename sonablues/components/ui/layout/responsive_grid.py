import reflex as rx

from sonablues.styles.tokens import (
    GRID_GAP,
)


DEFAULT_GRID_COLUMNS = {
    "base": "1",
    "sm": "2",
    "lg": "3",
    "2xl": "4",
}


def responsive_grid(
    *children,
    columns: dict | None = None,
    spacing: str = GRID_GAP,
    **props,
) -> rx.Component:
    return rx.grid(
        *children,
        columns=columns or DEFAULT_GRID_COLUMNS,
        spacing=spacing,
        width="100%",
        align_items="stretch",
        auto_rows="1fr",
        **props,
    )