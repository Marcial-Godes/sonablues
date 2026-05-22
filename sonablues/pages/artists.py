import reflex as rx
from sonablues.constants import (
    ARTISTS_TITLE,
)
from sonablues.components.base_layout import (
    base_layout,
)

from sonablues.components.protected_page import (
    protected_page,
)

from sonablues.components.layout import (
    page_container,
)
from sonablues.components.artist.artist_card import (
    artist_card,
)
from sonablues.services.artist_service import (
    get_artists_by_instrument,
)

from sonablues.components.ui.text import (
    page_title,
)

from sonablues.components.ui.layout import (
    content_stack,
    responsive_grid,
)


def artists_page(
    instrument_slug: str,
) -> rx.Component:
    artists = get_artists_by_instrument(
        instrument_slug,
    )
    return protected_page(
        base_layout(
            page_container(
                content_stack(
                    page_title(
                        ARTISTS_TITLE,
                    ),
                    responsive_grid(
                        *[
                            artist_card(artist)
                            for artist in artists
                        ],
                    ),
                )
            )
        )
    )