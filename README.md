We model this game using a few classes:

The `Knight` class will hold properties such as ID, position, items equipped, base attack, etc.

The `Arena` class will be mainly concerned with storing the positon of everything on the board and
launching attacks.

The `POS` class is used by both Knight and Arena to determine their position.

A `Serialize` and `Deserialize` class to read and write to the FS.

A `Battle` class which runs the deserialized instructions, updates the arena and positions, marks Knights as dead, etc.


# Outline of classes

## Knight dataclass:

    ID: R
    X: 0
    Y: 0
    Equiped: <item>
    BaseAttack: 1
    BaseDefence: 1

## Arena class:

### Properties

    board - 2 dimensional matrix
            each item is a POS element

### Methods

    move_knight - allowed (N,S,E,W)
        move_empty_square - update position
        move_square_with_loot - equip item, according to (A,M,D,H) rule
        move_square_with_knight - attack
        move_square_with_water - drown, drop items

## POS class:

    position: (0, 0)
    knight_ids: ()
    item_ids: ()

## Serialize class:

    serialize to JSON format and write to FS.

## Deserialize class:

    deserialize from move.txt file and run application


## Battle class:

    Run deserialized instructions and update Arena, Knights, etc.

