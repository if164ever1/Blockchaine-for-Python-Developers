import hashlib
import json


class Block:
    id = None
    history = None
    parent_id = None
    parent_hash = None

block_A = Block()
block_A.id = "A"
block_A.history = "Nelson likes cats."

block_B = Block()
block_B.id = "B"
block_B.history = "Maria likes dogs."
block_B.parent_id = block_A.id
block_B.parent_hash = hashlib.sha256(
    json.dumps(block_A.__dict__, sort_keys=True).encode('utf-8')).hexdigest()
print(block_B.parent_hash)

block_C = Block()
block_C.id = "C"
block_C.history = "Sky likes birds."
block_C.parent_id = block_B.id
block_C.parent_hash = hashlib.sha256(
    json.dumps(block_B.__dict__, sort_keys=True).encode('utf-8')).hexdigest()
print(block_C.parent_hash)

print(block_A.__dict__)
print(block_B.__dict__)
print(block_C.__dict__)

block_D = Block()
block_D.id = "D"
block_D.history = "Luna likes fish."
block_D.parent_id = block_C.id

block_serialized = json.dumps(block_D.__dict__).encode('utf-8')
print(block_serialized)

payload = block_serialized
for i in range(100000000):
    nonce = str(i).encode('utf-8')
    result  = hashlib.sha256(payload + nonce).hexdigest()
    if result.startswith('000000'):
        print(f"Success with nonce {i}")
        print(f"Hash is {result}")
        break
block_D.parent_hash = result
print(block_D.__dict__)