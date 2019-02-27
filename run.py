from arena import Arena
from knight import Knight
from item import Item

arena = Arena()
ab = arena.board


# Setup initial board with: knights, items, and positions.

kR = Knight('R', ab[0][0])
kB = Knight('B', ab[7][0])
kG = Knight('G', ab[7][7])
kY = Knight('Y', ab[0][7])

ab[0][0].knights.append(kR)
ab[7][0].knights.append(kB)
ab[7][7].knights.append(kG)
ab[0][7].knights.append(kY)


item_axe = Item('Axe', 4, ab[2][2], 2, 0)
item_dagger = Item('Dagger', 2, ab[2][5], 1, 0)
item_magicstaff = Item('MagicStaff', 3, ab[5][2], 1, 1)
item_helmet = Item('Helmet', 1, ab[5][5], 0, 1)

ab[2][2].items.append(item_axe)
ab[2][5].items.append(item_dagger)
ab[5][2].items.append(item_magicstaff)
ab[5][5].items.append(item_helmet)

