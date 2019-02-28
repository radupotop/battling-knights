# Battling Knights

Note: This requires `Python 3.7` to run since it leverages the new `@dataclass` notation.


We model this game using a few classes:

The `Knight` class will hold properties such as ID, position, items equipped, base attack, etc.

The `Arena` class will be mainly concerned with storing the positon of everything on the board and moving things around.

The `Item` class used to describe items on the board.

The `POS` class is the building block of the board; is used by both Knight and Arena to determine their position.

A `Battle` class which deals with the life and death of knights.

A `Serialize` and `Deserialize` class to read and write to the FS.

These classes reference each other like so:

A knight instance has a `pos` attribute so it always knows where it's placed on the board.
A `pos` instance always knows whether it holds _items_ or a _knight_.


# Outline of classes

## Knight class:

    ID: R
    pos: <Pos>
    equipped: <Item>
    BaseAttack: 1
    BaseDefence: 1

## Arena class:

**Properties**

    board - 2 dimensional matrix
            each item is a POS element

**Methods**

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


We are able to determine the position of a knight either by referring to `knight.pos`
or by referring to `arena.board`.

