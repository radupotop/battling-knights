from dataclasses import dataclass, field


@dataclass
class Pos:
    """
    This represents a 'square' on the board.
    """

    y: int
    x: int
    knight: dict = None
    items: list = field(default_factory=list)
