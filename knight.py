from dataclasses import dataclass, field

from item import Item
from pos import Pos


@dataclass
class Knight:
    id: str # One of: R,G,B,Y
    pos: Pos
    equipped: Item = None
    base_attack: int = 1
    base_defence: int = 1
