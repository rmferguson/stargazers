import random
from enum import Enum
from typing import List

__all__ = [
    "rand_enum_choice",
    "rand_enum_sample",
    "as_name_list",
    "as_enum_values",
]


def rand_enum_choice(e: Enum):
    return random.choice(list(e.__members__.values()))


def rand_enum_sample(e: Enum):
    tmp = list(e.__members__.values())
    return random.sample(tmp, random.randint(1, len(tmp)))


def as_name_list(enum_values: Enum):
    return [v.name.lower() for v in enum_values]


def as_enum_values(enum_type: Enum, name_list: List[str]):
    return [enum_type(n) for n in name_list]
