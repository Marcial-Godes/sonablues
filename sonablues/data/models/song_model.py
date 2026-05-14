from dataclasses import dataclass, field
from sonablues.data.models.difficulty import Difficulty


@dataclass
class Video:
    title: str
    youtube_id: str


@dataclass
class Song:
    title: str
    slug: str
    artist: str
    difficulty: Difficulty
    tuning: str
    techniques: list[str] = field(
        default_factory=list
    )
    videos: list[Video] = field(
        default_factory=list
    )
    image: str = ""