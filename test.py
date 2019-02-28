import unittest
from run import setup_board


class TestCase(unittest.TestCase):
    def setUp(self):
        (
            self.arena,
            self.kR,
            self.kY,
            self.kB,
            self.kG,
            self.item_axe,
            self.item_dagger,
            self.item_magicstagg,
            self.item_helmet,
        ) = setup_board()

    def testKnightMoves(self):
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'E')
        self.arena.move_knight(self.kR, 'E')

        self.assertEqual(self.kR.pos.x, 2)
        self.assertEqual(self.kR.pos.y, 2)
        self.assertEqual(self.kR.equipped, self.item_axe)

        self.assertEqual(len(self.arena.board[2][2].items), 0)
        self.assertEqual(self.arena.board[2][2].knight, self.kR)

    def testKnightBattle(self):
        self.arena.move_knight(self.kR, 'E')
        self.arena.move_knight(self.kR, 'E')

        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')
        self.arena.move_knight(self.kR, 'S')

        self.arena.move_knight(self.kR, 'W')
        self.arena.move_knight(self.kR, 'W')

        self.assertEqual(self.kR.pos.x, 0)
        self.assertEqual(self.kR.pos.y, 7)

        self.assertEqual(self.kR.status, 'LIVE')

        self.assertEqual(self.kB.status, 'DEAD')


if __name__ == '__main__':
    unittest.main(verbosity=2)
