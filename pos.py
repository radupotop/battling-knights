from dataclasses import dataclass, field

@dataclass
class Pos:
    """
    This represents a 'square' on the board.
    """
    x: int
    y: int
    knights: list = field(default_factory=list)
    items: list = field(default_factory=list)
