from typing import TypedDict, List


class Hero(TypedDict):
    id: int
    name: str
    localized_name: str
    primary_attr: str
    attack_type: str
    roles: List[str]
    legs: int
