from dataclasses import dataclass, field


def empty_matrix():
    return [[], [], [], [], [], [], [], []]


@dataclass
class Arena:
    board: list = field(default_factory=empty_matrix)

    def move_knight(knight, direction):
        pass

    def _direction_to_pos(direction, old_pos):
        pass

    def _is_empty_square(pos):
        return len(pos.knights) + len(pos.items) == 0

    def _is_square_with_item(pos):
        return len(pos.items) > 0

    def _is_square_with_knight(pos):
        return len(pos.knights) > 0

    def _is_square_with_water(pos):
        return (pos.x < 0 or pos.x > 8) and (pos.y < 0 or pos.y > 8)
