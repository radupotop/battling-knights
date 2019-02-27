from dataclasses import dataclass, field

from pos import Pos


class Arena:
    """
    The Arena class handles movement of its knights and items.

    The `board` property is a matrix of Pos elements.
    """
    def __init__(self):
        board = []
        for x in range(0, 8):
            row = []
            for y in range(0, 8):
                row.append(Pos(x, y))
            board.append(tuple(row))

        self.board = tuple(board)

    def move_knight(self, knight, direction):
        x, y = self._direction_to_xy(direction, knight.pos)

    def _direction_to_xy(self, direction: str, old_pos: Pos):
        dir_map = {
            'N': (old_pos.x, old_pos.y - 1),
            'S': (old_pos.x, old_pos.y + 1),
            'E': (old_pos.x + 1, old_pos.y),
            'W': (old_pos.x - 1, old_pos.y),
        }
        return dir_map[direction]

    def _is_empty_square(self, pos):
        return len(pos.knights) + len(pos.items) == 0

    def _is_square_with_item(self, pos):
        return len(pos.items) > 0

    def _is_square_with_knight(self, pos):
        return len(pos.knights) > 0

    def _is_square_with_water(self, pos):
        return (pos.x < 0 or pos.x > 8) and (pos.y < 0 or pos.y > 8)
