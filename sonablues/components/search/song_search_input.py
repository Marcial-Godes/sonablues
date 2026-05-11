import reflex as rx

from sonablues.states.song_search_state import (
    SongSearchState,
)

from sonablues.styles.theme import (
    CARD_COLOR,
    CARD_BORDER,
)


def song_search_input() -> rx.Component:

    return rx.input(

        placeholder="Search songs, techniques or difficulty...",

        value=SongSearchState.search_text,

        on_change=SongSearchState.set_search,

        width="100%",

        size="3",

        background=CARD_COLOR,

        border=CARD_BORDER,
    )