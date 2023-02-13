import datetime
from hashlib import sha256

import uuid # generate a nonce with uuid, you can also generate a nonce with secret or with the random method, or by incrementing by one

import calendar #datetime
import time
from datetime import datetime


current_GMT = time.gmtime()
time_stamp = calendar.timegm(current_GMT)
print("Current timestamp:", time_stamp)
time = datetime.fromtimestamp(time_stamp)
print("time =", time)


class Block():
    data = None
    hash = None
    index = None
    time = None
    nonce = 0
    previous_hash = "0" * 64

    #initialize the block
    def __init__(self,data,index=0):
        self.data = data
        self.index = index

    #generate the hash of the block
    def hash(self):
        h = sha256()
        hashing_text = str(self.data) + str(self.hash) + str(self.index) + str(time) + str(self.nonce) + str(self.previous_hash)
        h.update(hashing_text.encode('utf-8'))
        return h.hexdigest()

   
    #display block infos
    def __str__(self):
        return str("Block \nindex: %s\nData: %s\nhash: %s\nTimestamp: %s\nNonce: %s\nPrevious_hash: %s" %(
        self.index,
        self.data,
        self.hash(),
        time,
        self.nonce,
        self.previous_hash
        ))

class Blockchain():
    difficulty = 4

    def __init__(self,chain=[]):
        self.chain = chain

    def add_a_block(self, block):
        self.chain.append(block)

    def get_last_block(self):
        print(self.chain[-1])

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError: pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add_a_block(block); break
            else:
                block.nonce = uuid.uuid4().hex

    def isValid(self):
        for i in range(1,len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty] != "0" * self.difficulty:
                return False

        return True



def main():
    blockchain = Blockchain()
    database = [{ "amount": 400}, {"amount": 100}, {"amount": 50},{"amount": 600}]

    index = 0

    for data in database:
        index += 1
        blockchain.mine(Block(data,index))

    for block in blockchain.chain:
        print(block)

    # testing if the blockchain is valid :
    # blockchain.chain[1].data = "NEW DATA"
    # blockchain.mine(blockchain.chain[2])

    for block in blockchain.chain:
        print("\n")
        print(block)
        


    #blockchain.get_last_block()    

    #print(blockchain.isValid())

if __name__ == '__main__':
    main()





