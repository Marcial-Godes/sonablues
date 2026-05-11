from dataclasses import dataclass


@dataclass
class Video:
    title: str
    youtube_id: str


@dataclass
class Song:
    title: str
    slug: str
    difficulty: str
    tuning: str
    techniques: list[str]
    videos: list[Video]
    image: str