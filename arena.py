from dataclasses import dataclass, field


def empty_matrix():
    return [[], [], [], [], [], [], [], []]

@dataclass
class Arena:
    board: list = field(default_factory=empty_matrix)

    def move_knight():
        pass
