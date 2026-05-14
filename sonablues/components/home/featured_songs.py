import reflex as rx
from sonablues.routes.routes import (
    song_detail_route,
)
from sonablues.services.song_service import (
    get_featured_songs,
)
from sonablues.components.ui import (
    muted_text,
    surface,
    cover_image,
)


def song_card(
    image_src: str,
    title: str,
    artist: str,
    difficulty: str,
    slug: str,
) -> rx.Component:
    return rx.link(
        surface(
            rx.vstack(
                cover_image(
                    src=image_src,
                    height={
                        "base": "170px",
                        "md": "220px",
                        "lg": "180px",
                    },
                    object_position="center top",
                ),
                rx.vstack(
                    rx.badge(
                        difficulty,
                        color_scheme=rx.cond(
                            difficulty == "Beginner",
                            "green",
                            rx.cond(
                                difficulty == "Intermediate",
                                "orange",
                                "red",
                            ),
                        ),
                        variant="soft",
                    ),
                    rx.heading(
                        title,
                        size="5",
                        line_height="1.1",
                    ),
                    muted_text(
                        artist,
                        size="3",
                    ),
                    spacing="1",
                    align="start",
                    width="100%",
                ),
                spacing="4",
                align="start",
                width="100%",
            ),
            padding={
                "base": "0.75rem",
                "md": "1rem",
            },
            width="100%",
            overflow="hidden",
            hoverable=True,
        ),
        href=song_detail_route(slug),
        width="100%",
        text_decoration="none",
    )


def featured_songs() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading(
                "Canciones destacadas",
                size={
                    "base": "5",
                    "md": "7",
                },
                text_align="center",
                width="100%",
            ),
            muted_text(
                "Aprende algunos de los riffs y canciones más icónicos.",
                size="4",
                text_align="center",
                max_width="32ch",
            ),
            spacing="3",
            align="center",
            width="100%",
        ),
        rx.grid(
            rx.foreach(
                get_featured_songs(),
                lambda song: song_card(
                    song.image,
                    song.title,
                    song.artist,
                    song.difficulty,
                    song.slug,
                ),
            ),
            columns={
                "base": "1",
                "md": "2",
                "lg": "3",
            },
            spacing="6",
            width="100%",
        ),
        spacing="7",
        width="100%",
        padding_y={
            "base": "1rem",
            "lg": "2rem",
        },
        margin_top={
            "base": "1.5rem",
            "lg": "0",
        },
    )