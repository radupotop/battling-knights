from dataclasses import dataclass, field

@dataclass
class Pos:
    """
    This represents a 'square' on the board.
    """
    x: int
    y: int
    knights: set = field(default_factory=set)
    items: set = field(default_factory=set)
