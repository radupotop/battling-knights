import unittest

from run import RunGame


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
        ) = RunGame().setup_board()

    def tearDown(self):
        self.arena.render()

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

    def testKnightDrown(self):
        self.arena.move_knight(self.kY, 'N')
        self.assertEqual(self.kY.status, 'DROWNED')

        self.arena.move_knight(self.kG, 'E')
        self.assertEqual(self.kG.status, 'DROWNED')


if __name__ == '__main__':
    unittest.main(verbosity=2)
