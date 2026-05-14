from enum import StrEnum


class Difficulty(StrEnum):
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"


DIFFICULTY_ORDER = {
    Difficulty.BEGINNER: 1,
    Difficulty.INTERMEDIATE: 2,
    Difficulty.ADVANCED: 3,
}