from dataclasses import dataclass


@dataclass
class Artist:
    name: str
    slug: str
    description: str
    image: str