import hashlib
import time
class Block:
    def __init__(self,index,data,prev_hash):
        self.index=index
        self.data=data
        self.prev_hash=prev_hash
        self.timestamp=time.time()
        self.hash=self.calculate_hash()
    def calculate_hash(self):
        text=str(self.index)+str(self.data)+str(self.prev_hash)+str(self.timestamp)
        return hashlib.sha256(text.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain=[self.create_genesis_block()]
    def create_genesis_block(self):
        return Block(0,"Genesis Block","0")
    def add_block(self,data):
        last=self.chain[-1]
        new_block=Block(
            len(self.chain),
            data,
            last.hash
        )
        self.chain.append(new_block)