import reflex as rx

from sonablues.constants import (
    SONG_NOT_FOUND,
)

from sonablues.components.layouts import (
    base_layout,
)

from sonablues.components.song import (
    song_hero,
    song_video_section,
    planned_content,
)

from sonablues.components.ui import (
    empty_state,
)

from sonablues.services import (
    get_song,
)

from sonablues.styles.spacing import (
    PAGE_GAP,
)

from sonablues.states.auth_state import (
    AuthState,
)


def song_detail_page(
    song_slug: str,
) -> rx.Component:

    song = get_song(song_slug)

    if not song:

        return base_layout(

            empty_state(
                title=SONG_NOT_FOUND,

                description=(
                    "The requested lesson does not exist "
                    "or is currently unavailable."
                ),
            )
        )

    return base_layout(

        rx.vstack(

            song_hero(song),

            rx.button(

                rx.cond(

                    AuthState.favorite_songs_list.contains(
                        song.slug
                    ),

                    "Remove from favorites",

                    "Add to favorites",
                ),

                on_click=lambda: AuthState.toggle_favorite(
                    song.slug,
                ),

                size="3",
            ),

            song_video_section(song),

            planned_content(),

            spacing=PAGE_GAP,
            align="start",
            width="100%",
        )
    )