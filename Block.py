


class Block:
    id = None
    previous_block = None
    history = None

block_A = Block()
block_A.id = "A"
block_A.history = "Nelson likes cats."

block_B = Block()
block_B.id = "B"
block_B.previous_block = block_A
block_B.history = "Maria likes dogs."

block_C = Block()
block_C.id = "C"
block_C.previous_block = block_B
block_C.history = "Sky likes birds."