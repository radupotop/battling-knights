from dataclasses import dataclass, field

from pos import Pos


def empty_matrix():
    return [[], [], [], [], [], [], [], []]


@dataclass
class Arena:
    """
    The Arena class handles movement of its knights and items.
    """

    board: list = field(default_factory=empty_matrix)

    def move_knight(knight, direction):
        pass

    def _direction_to_xy(direction: str, old_pos: Pos):
        dir_map = {
            'N': (old_pos.x, old_pos.y - 1),
            'S': (old_pos.x, old_pos.y + 1),
            'E': (old_pos.x + 1, old_pos.y),
            'W': (old_pos.x - 1, old_pos.y),
        }
        return dir_map[direction]

    def _is_empty_square(pos):
        return len(pos.knights) + len(pos.items) == 0

    def _is_square_with_item(pos):
        return len(pos.items) > 0

    def _is_square_with_knight(pos):
        return len(pos.knights) > 0

    def _is_square_with_water(pos):
        return (pos.x < 0 or pos.x > 8) and (pos.y < 0 or pos.y > 8)
