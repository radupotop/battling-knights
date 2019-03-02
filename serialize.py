from pathlib import Path
from json import dumps


class Serialize:
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

        for k in knights:
            k_result = (k.pos.to_json() if k.pos else None, k.status)
            if k.equipped:
                k_result += (
                    k.equipped.name,
                    k.base_attack + k.equipped.attack,
                    k.base_defence + k.equipped.defence,
                )
            else:
                k_result += (None, k.base_attack, k.base_defence)
            result[k.colour] = k_result

        for i in items:
            i_result = (i.pos.to_json(), i.pos.knight is not None)
            result[i.name] = i_result

        return result

    @staticmethod
    def commit_to_fs(state):
        return Path('./final_state.json').write_text(dumps(state))
