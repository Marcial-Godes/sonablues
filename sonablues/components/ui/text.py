import reflex as rx

from sonablues.styles.theme import (
    TEXT_COLOR,
    MUTED_TEXT,
)

from sonablues.styles.tokens import (
    TITLE_SIZE_CARD,
    TEXT_SIZE_SECONDARY,
    TEXT_SIZE_BODY,
    TEXT_SIZE_SMALL,
)


def base_text(
    component,
    text: str,
    default_props: dict,
    **props,
) -> rx.Component:
    return component(
        text,
        **{
            **default_props,
            **props,
        },
    )
    
    
def title_text(
    text: str,
    **props,
) -> rx.Component:
    default_props = {
        "color": TEXT_COLOR,
        "size": TITLE_SIZE_CARD,
        "width": "100%",
    }
    return base_text(
        rx.heading,
        text,
        default_props,
        **props,
    )


def body_text(
    text: str,
    **props,
) -> rx.Component:
    default_props = {
        "color": TEXT_COLOR,
        "size": TEXT_SIZE_BODY,
        "width": "100%",
    }
    return base_text(
        rx.text,
        text,
        default_props,
        **props,
    )


def secondary_text(
    text: str,
    **props,
) -> rx.Component:
    default_props = {
        "color": MUTED_TEXT,
        "size": TEXT_SIZE_SECONDARY,
        "width": "100%",
    }
    return base_text(
        rx.text,
        text,
        default_props,
        **props,
    )


def caption_text(
    text: str,
    **props,
) -> rx.Component:
    default_props = {
        "color": MUTED_TEXT,
        "size": TEXT_SIZE_SMALL,
        "width": "100%",
    }

    return base_text(
        rx.text,
        text,
        default_props,
        **props,
    )
    
    
def label_text(
    text: str,
    **props,
) -> rx.Component:
    default_props = {
        "color": TEXT_COLOR,
        "size": TEXT_SIZE_SMALL,
        "weight": "bold",
        "width": "100%",
    }

    return base_text(
        rx.text,
        text,
        default_props,
        **props,
    )