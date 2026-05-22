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
    DISPLAY_TITLE_SIZE,
    SECTION_TITLE_SIZE,
    CARD_TITLE_SIZE,
)

from sonablues.styles.fonts import (
    HEADING_FONT,
    BODY_FONT,
)


def base_text(
    component,
    text: str,
    width: str = "100%",
    **props,
) -> rx.Component:
    return component(
        text,
        width=width,
        **props,
    )


def title_text(
    text: str,
    size: str = TITLE_SIZE_CARD,
    color: str = TEXT_COLOR,
    **props,
) -> rx.Component:

    props.setdefault(
        "font_family",
        HEADING_FONT,
    )

    props.setdefault(
        "font_weight",
        "400",
    )

    props.setdefault(
        "letter_spacing",
        "-0.02em",
    )

    props.setdefault(
        "line_height",
        "1.1",
    )

    return base_text(
        rx.heading,
        text,
        size=size,
        color=color,
        **props,
    )


def body_text(
    text: str,
    size: str = TEXT_SIZE_BODY,
    color: str = TEXT_COLOR,
    **props,
) -> rx.Component:
    
    props.setdefault(
        "font_family",
        BODY_FONT,
    )
    
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        **props,
    )


def secondary_text(
    text: str,
    size: str = TEXT_SIZE_SECONDARY,
    color: str = MUTED_TEXT,
    **props,
) -> rx.Component:
    
    props.setdefault(
        "font_family",
        BODY_FONT,
    )
    
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        **props,
    )


def caption_text(
    text: str,
    size: str = TEXT_SIZE_SMALL,
    color: str = MUTED_TEXT,
    **props,
) -> rx.Component:
    
    props.setdefault(
        "font_family",
        BODY_FONT,
    )
    
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        **props,
    )


def label_text(
    text: str,
    size: str = TEXT_SIZE_SMALL,
    color: str = TEXT_COLOR,
    weight: str = "bold",
    **props,
) -> rx.Component:
    
    props.setdefault(
        "font_family",
        BODY_FONT,
    )
    
    return base_text(
        rx.text,
        text,
        size=size,
        color=color,
        weight=weight,
        **props,
    )
    

def display_title(
    text: str,
    line_height: str = "0.95",
    **props,
) -> rx.Component:
    return title_text(
        text,
        size=DISPLAY_TITLE_SIZE,
        line_height=line_height,
        **props,
    )


def section_title(
    text: str,
    **props,
) -> rx.Component:
    return title_text(
        text,
        size=SECTION_TITLE_SIZE,
        line_height="1.05",
        **props,
    )


def card_title(
    text: str,
    **props,
) -> rx.Component:
    return title_text(
        text,
        size=CARD_TITLE_SIZE,
        line_height="1.1",
        **props,
    )