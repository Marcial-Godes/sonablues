import reflex as rx

from sonablues.app_pages import (
    register_pages,
)

from sonablues.styles.fonts import (
    BODY_FONT,
)


app = rx.App(
    style={
        "font_family": BODY_FONT,
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@200..800&display=swap",
    ],
)

register_pages(app)