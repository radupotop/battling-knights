from dataclasses import dataclass

@dataclass
class Pos:
    """
    This represents a 'square' on the board.
    """
    x: int
    y: int
    knights: set
    items: set
