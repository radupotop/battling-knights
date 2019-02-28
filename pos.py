from dataclasses import dataclass, field

@dataclass
class Pos:
    """
    This represents a 'square' on the board.
    """
    x: int
    y: int
    knight: dict = None
    items: list = field(default_factory=list)
