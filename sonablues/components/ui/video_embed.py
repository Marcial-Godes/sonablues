import reflex as rx

from sonablues.styles.tokens import (
    CARD_RADIUS,
)


def video_embed(
    src: str,
    aspect_ratio: str = "56.25%",
    **props,
) -> rx.Component:
    return rx.box(
        rx.html(
            f"""
            <iframe
                src="{src}"
                title="YouTube video player"
                frameborder="0"
                allowfullscreen
                style="
                    position:absolute;
                    top:0;
                    left:0;
                    width:100%;
                    height:100%;
                    border:none;
                    border-radius:{CARD_RADIUS};
                "
            ></iframe>
            """
        ),
        position="relative",
        width="100%",
        padding_top=aspect_ratio,
        overflow="hidden",
        border_radius=CARD_RADIUS,
        **props,
    )