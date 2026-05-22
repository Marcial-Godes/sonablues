import reflex as rx


def difficulty_badge(
    difficulty: str,
    size: str = "2",
) -> rx.Component:

    color_scheme = rx.cond(
        difficulty == "Beginner",
        "green",

        rx.cond(
            difficulty == "Intermediate",
            "orange",
            "red",
        ),
    )

    return rx.badge(
        difficulty,
        size=size,
        color_scheme=color_scheme,
        variant="soft",
    )