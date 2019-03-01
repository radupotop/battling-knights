import json
from dataclasses import dataclass, field

from item import Item
from pos import Pos


STATUS_OPTS = ('LIVE', 'DEAD', 'DROWNED')


@dataclass
class Knight:
    id: str  # One of: R,G,B,Y
    colour: str
    pos: Pos
    status: str = STATUS_OPTS[0]
    equipped: Item = None
    base_attack: int = 1
    base_defence: int = 1

    def update_status(self, idx):
        self.status = STATUS_OPTS[idx]
