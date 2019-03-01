from pathlib import Path
from json import dumps

class Deserialize:
    @staticmethod
    def read_moves():
        """
        Read moves from file and output instructions.
        """
        _contents = Path('./moves.txt').read_text()
        moves = _contents.strip().split('\n')
        if moves[0] == 'GAME-START':
            moves.pop(0)
        if moves[-1] == 'GAME-END':
            moves.pop()
        return tuple(tuple(m.split(':')) for m in moves)

    @staticmethod
    def serialize_gamestate(knights: list, items: list):
        result = {}
        _format_str = '{}, "{}", "{}", {}, {}'
        for k in knights:
            if k.equipped:
                result[k.colour] = _format_str.format(
                    k.pos if k.pos else 'null',
                    k.status,
                    k.equipped.name,
                    k.base_attack + k.equipped.attack,
                    k.base_defence + k.equipped.defence,
                )
            else:
                result[k.colour] = _format_str.format(
                    k.pos if k.pos else 'null',
                    k.status,
                    'null',
                    k.base_attack,
                    k.base_defence,
                )

        return result

    @staticmethod
    def commit_to_fs(state):
        pass
