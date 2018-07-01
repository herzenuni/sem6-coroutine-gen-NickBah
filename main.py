import hashlib as hasher
import datetime


class Block:
    def __init__(self, index,timestamp,data,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    """ Функция для создания нового блока """
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

def create_first_block():
    return Block(0,datetime.datetime.now(),"First Block",None)


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = 'Block ' + str(this_index)
    this_lasthash = last_block.hash
    return Block(this_index,this_timestamp,this_data,this_lasthash)

def run_blocks_generator():
    history = [create_first_block()]
    i = 0
    while True:
        block = next_block(history[i])

        i += 1
        history.append(block)
        yield block

blocks = run_blocks_generator()

blocks.send(None)

for i in range(5):
    b = blocks.send(None)
    print(b.index)
    print(b.data)
    print(b.hash)
    print()

blocks.close()
