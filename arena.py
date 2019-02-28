from dataclasses import dataclass, field
from operator import attrgetter

from pos import Pos
from battle import Battle


class Arena:
    """
    The Arena class handles movement of its knights and items.

    The `board` property is a matrix of Pos elements.
    """

    def __init__(self):
        board = []
        for y in range(0, 8):
            row = [Pos(y, x) for x in range(0, 8)]
            board.append(tuple(row))

        self.board = tuple(board)

    def move_knight(self, knight, direction):
        _pos = self._direction_to_pos(direction, knight.pos)

        # clear out the old position square
        knight.pos.knight = None

        if self._is_empty_square(_pos):
            knight.pos = _pos
            _pos.knight = knight
            print('Moved', knight)
        elif self._is_square_with_item(_pos):
            knight.pos = _pos
            _pos.items.sort(key=attrgetter('priority'))
            knight.equipped = _pos.items.pop()
            _pos.knight = knight
            print('Acquired item', knight)
        elif self._is_square_with_water(_pos):
            loot = Battle.kill_knight(knight, status=2)
            _pos.items.append(loot)
            _pos.knight = None
            print('Drowned', knight)
        elif self._is_square_with_knight(_pos):
            # Battle!
            print('Attack ', knight)
            winner, loser = Battle.attack(knight, _pos.knight)
            loot = Battle.kill_knight(loser)
            winner.pos = _pos
            _pos.items.append(loot)
            _pos.knight = winner
            print('## BATTLE ##')
            print('Winner:', winner)
            print('Loser:', loser)
            return winner

        return knight

    def render(self):
        print('')
        for row in self.board:
            for pos in row:
                if pos.knight:
                    print('🦁' + pos.knight.id, end='')
                elif len(pos.items):
                    print('🗡' + pos.items[0].name[0], end='')
                else:
                    print('  ', end='')
            print('')
        print('')

    def _direction_to_pos(self, direction: str, old_pos: Pos):
        dir_map = {
            'N': (old_pos.y - 1, old_pos.x),
            'S': (old_pos.y + 1, old_pos.x),
            'E': (old_pos.y, old_pos.x + 1),
            'W': (old_pos.y, old_pos.x - 1),
        }
        y, x = dir_map[direction]
        return self.board[y][x]

    def _is_empty_square(self, pos):
        return not pos.knight and len(pos.items) is 0

    def _is_square_with_item(self, pos):
        return len(pos.items) > 0

    def _is_square_with_knight(self, pos):
        return pos.knight is not None

    def _is_square_with_water(self, pos):
        return (pos.x < 0 or pos.x > 8) and (pos.y < 0 or pos.y > 8)
