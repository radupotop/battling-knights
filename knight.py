import json
from dataclasses import dataclass, field

from item import Item
from pos import Pos


STATUS_OPTS = ('LIVE', 'DEAD', 'DROWNED')

@dataclass
class Knight:
    id: str # One of: R,G,B,Y
    pos: Pos
    status: str = STATUS_OPTS[0]
    equipped: Item = None
    base_attack: int = 1
    base_defence: int = 1

    def __json__(self):
        return [
            '[{}, {}]'.format(self.pos.x, self.pos.y),
            '"{}"'.format(self.status),
            self.equipped.name if self.equipped else None,
            self.base_attack,
            self.base_defence
        ]
