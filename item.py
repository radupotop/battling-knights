from dataclasses import dataclass

from pos import Pos


@dataclass
class Item:
    name: str
    priority: int  # A,M,D,H -> 4,3,2,1
    pos: Pos
    attack: int
    defence: int
