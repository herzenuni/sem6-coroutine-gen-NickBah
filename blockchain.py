import hashlib as hasher
import datetime as date
import string


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """ Конструктор нового объекта """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        
    def hash_block(self):
        """ Функция для создания нового блока """
        sha = hasher.sha256()
        data = (str(self.index) + str(self.timestamp) + 
                   str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update(data)
        return sha.hexdigest()
    
    
def create_genesis_block():
    
    return Block(0, date.datetime.now(), "This is first block data", str(0))


def next_block(last_block):
    current_index = last_block.index + 1
    
    current_timestamp = date.datetime.now()
    
    current_data = str(current_index) + string.ascii_lowercase

    current_hash = last_block.hash
    
    return Block(current_index, current_timestamp, current_data, current_hash)


blockchain = [create_genesis_block()]

number_of_blocks = 10

for i in range(10):
    new_block = next_block(blockchain[i])
    blockchain.append(new_block)
    print(f"Data: {new_block.data}, New block is : {new_block.hash} \n")