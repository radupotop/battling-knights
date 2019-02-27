from dataclasses import dataclass

@dataclass
class Item:
    name: str
    priority: int # A,M,D,H -> 0,1,2,3
    attack: int
    defence: int
