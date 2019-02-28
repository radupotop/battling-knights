from pathlib import Path


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
