import os
from pathlib import Path


def load_directions(direction_dir: Path) -> list:
    directions = []
    for direction_file in os.listdir(direction_dir):
        with open(direction_dir / direction_file, "r", encoding="utf-8") as fp:
            directions.append(fp.read())
    return directions


def convert_to_prompt(directions: list):
    return [
        {
            "role": "user",
            "content": direction,
        }
        for direction in directions
    ]


def parse_all_sections(*args):
    rlt = []
    for arg in args:
        rlt = rlt + arg
    return rlt


DIRECTION_HOME = Path(".") / "oai" / "data" / "directions"
SECTOR_1_DIRECTION_HOME = DIRECTION_HOME / "1"
SECTOR_2_DIRECTION_HOME = DIRECTION_HOME / "2"
SECTOR_3_DIRECTION_HOME = DIRECTION_HOME / "3"


SECTOR_1_DIRECTIONS = load_directions(SECTOR_1_DIRECTION_HOME)
SECTOR_2_DIRECTIONS = load_directions(SECTOR_2_DIRECTION_HOME)
SECTOR_3_DIRECTIONS = load_directions(SECTOR_3_DIRECTION_HOME)
ALL_SECTOR_DIRECTIONS = parse_all_sections(
    SECTOR_1_DIRECTIONS,
    SECTOR_2_DIRECTIONS,
    SECTOR_3_DIRECTIONS,
)

SECTOR_1_DIRECTION_PROMPTS = convert_to_prompt(SECTOR_1_DIRECTIONS)
SECTOR_2_DIRECTION_PROMPTS = convert_to_prompt(SECTOR_2_DIRECTIONS)
SECTOR_3_DIRECTION_PROMPTS = convert_to_prompt(SECTOR_3_DIRECTIONS)
ALL_SECTOR_DIRECTION_PROMPTS = parse_all_sections(
    SECTOR_1_DIRECTION_PROMPTS,
    SECTOR_2_DIRECTION_PROMPTS,
    SECTOR_3_DIRECTION_PROMPTS,
)


__all__ = [
    "SECTOR_1_DIRECTION_HOME",
    "SECTOR_2_DIRECTION_HOME",
    "SECTOR_3_DIRECTION_HOME",
    "SECTOR_1_DIRECTIONS",
    "SECTOR_2_DIRECTIONS",
    "SECTOR_3_DIRECTIONS",
    "ALL_SECTOR_DIRECTIONS",
    "SECTOR_1_DIRECTION_PROMPTS",
    "SECTOR_2_DIRECTION_PROMPTS",
    "SECTOR_2_DIRECTION_PROMPTS",
    "ALL_SECTOR_DIRECTION_PROMPTS",
]
