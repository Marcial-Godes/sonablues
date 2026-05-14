import reflex as rx

from sonablues.styles.sizes import (
    GRID_SPACING,
)


def responsive_grid(
    *children,
    columns: dict | None = None,
    **props,
) -> rx.Component:

    default_columns = {
        "base": "1",
        "md": "2",
        "lg": "3",
    }

    return rx.grid(

        *children,

        columns=columns or default_columns,

        spacing=GRID_SPACING,

        width="100%",

        **props,
    )