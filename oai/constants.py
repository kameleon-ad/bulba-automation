import os
from pathlib import Path


def load_directions(direction_dir: Path) -> list:
    directions = []
    for direction_file in os.listdir(direction_dir):
        with open(direction_dir / direction_file, "r", encoding="utf-8") as fp:
            directions.append(fp.read())
    return directions


def convert_to_prompt(directions: list, role: str):
    return [
        {
            "role": role,
            "content": direction,
        }
        for direction in directions
    ]


def parse_all_sections(*args):
    rlt = []
    for arg in args:
        rlt = rlt + arg
    return rlt


def load_example(example_dir: Path):
    user_prompt = []
    for type_prompt in ["prompt", "response_a", "response_b"]:
        with open(example_dir / f"{type_prompt}.md", "r", encoding="utf8") as fp:
            user_prompt.append(type_prompt)
            user_prompt.append(fp.read())
    user_prompt = convert_to_prompt(user_prompt, "user")

    with open(example_dir / "answer.md", "r", encoding="utf-8") as fp:
        assisstant_prompt = [
            fp.read()
        ]
    return user_prompt + convert_to_prompt(assisstant_prompt, "assisstant")


def load_examples(examples_dir: Path):
    examples = []
    for example_dir in os.listdir(examples_dir):
        examples += load_example(examples_dir / example_dir)
    return examples


DATA_HOME = Path(".") / "oai" / "data"
DIRECTION_HOME = DATA_HOME / "directions"
EXAMPLE_HOME = DATA_HOME / "examples"
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

SECTOR_1_DIRECTION_PROMPTS = convert_to_prompt(SECTOR_1_DIRECTIONS, "user")
SECTOR_2_DIRECTION_PROMPTS = convert_to_prompt(SECTOR_2_DIRECTIONS, "user")
SECTOR_3_DIRECTION_PROMPTS = convert_to_prompt(SECTOR_3_DIRECTIONS, "user")
ALL_SECTOR_DIRECTION_PROMPTS = parse_all_sections(
    SECTOR_1_DIRECTION_PROMPTS,
    SECTOR_2_DIRECTION_PROMPTS,
    SECTOR_3_DIRECTION_PROMPTS,
)
EXAMPLE_PROMPTS = load_examples(EXAMPLE_HOME)
DEFAULT_PROMPTS = ALL_SECTOR_DIRECTION_PROMPTS + EXAMPLE_PROMPTS


__all__ = [
    "SECTOR_1_DIRECTION_HOME",
    "SECTOR_2_DIRECTION_HOME",
    "SECTOR_3_DIRECTION_HOME",
    "EXAMPLE_HOME",
    "SECTOR_1_DIRECTIONS",
    "SECTOR_2_DIRECTIONS",
    "SECTOR_3_DIRECTIONS",
    "ALL_SECTOR_DIRECTIONS",
    "SECTOR_1_DIRECTION_PROMPTS",
    "SECTOR_2_DIRECTION_PROMPTS",
    "SECTOR_2_DIRECTION_PROMPTS",
    "ALL_SECTOR_DIRECTION_PROMPTS",
    "EXAMPLE_PROMPTS",
    "DEFAULT_PROMPTS",
]
