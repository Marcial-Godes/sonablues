import reflex as rx
from sonablues.states.song_search_state import (
    SongSearchState,
)
from sonablues.styles.theme import (
    CARD_COLOR,
    CARD_BORDER,
    TEXT_COLOR,
    MUTED_TEXT,
    ACCENT_COLOR,
    ACCENT_BACKGROUND,
)
from sonablues.styles.radius import (
    INPUT_RADIUS,
    
)
from sonablues.styles.layout import (
    SEARCH_WIDTH
)
from sonablues.styles.transitions import (
    FAST_TRANSITION
)
from sonablues.styles.tokens import (
    INPUT_ICON_SIZE,
    )


def song_search_input() -> rx.Component:
    return rx.box(

        rx.image(
        src="/icons/search.svg",
        width=INPUT_ICON_SIZE,
        height=INPUT_ICON_SIZE,
        position="absolute",
        left="14px",
        top="50%",
        transform="translateY(-50%)",
        pointer_events="none",
        z_index="1",
    ),

        rx.input(

            placeholder="Search songs, techniques or difficulty...",

            value=SongSearchState.search_text,

            on_change=SongSearchState.set_search,

            width="100%",

            size="3",

            background=CARD_COLOR,

            border=CARD_BORDER,

            border_radius=INPUT_RADIUS,

            color=TEXT_COLOR,

            padding_left="2.5rem",

            padding_right="1rem",

            transition=FAST_TRANSITION,

            _placeholder={
                "color": "#7F8C99",
            },

            _hover={
                "border": f"1px solid {ACCENT_COLOR}",
            },

            _focus={
                "border": f"1px solid {ACCENT_COLOR}",
                "background": ACCENT_BACKGROUND,
                "box_shadow": "none",
            },
        ),
        position="relative",
        width="100%",
        max_width=SEARCH_WIDTH,
        margin="12px auto 0 0",
    )