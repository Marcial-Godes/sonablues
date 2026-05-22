import reflex as rx

from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.protected_page import (
    protected_page,
)

from sonablues.components.layout import (
    page_container,
)

from sonablues.components.search import (
    song_search_input,
)

from sonablues.components.song import (
    song_card,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)

from sonablues.components.ui.sections import (
    page_header,
)

from sonablues.components.ui.feedback import (
    empty_state,
)

from sonablues.services.artist_service import (
    get_artist,
)

from sonablues.states.song_search_state import (
    SongSearchState,
)


def songs_page(
    artist_slug: str,
) -> rx.Component:

    artist = get_artist(
        artist_slug,
    )

    return protected_page(
        base_layout(
            page_container(
                content_stack(
                    page_header(
                        title=artist.name,
                        description=artist.description,
                    ),

                    song_search_input(),

                    rx.cond(
                        SongSearchState.filtered_songs.length() > 0,

                        responsive_grid(
                            rx.foreach(
                                SongSearchState.filtered_songs,
                                lambda song: song_card(song),
                            ),
                        ),

                        empty_state(
                            title="No songs found",
                            description=(
                                "Try another search term."
                            ),
                        ),
                    ),

                    on_mount=SongSearchState.load_songs(
                        artist_slug,
                    ),
                )
            )
        )
    )