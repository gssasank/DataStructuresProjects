import hashlib

from datetime import datetime


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.data = data
        self.previous_hash = previous_hash
        self.hash = calc_hash(data)
        self.next = None  # Adding this line to make it easier to implement as a Linked List


class Blockchain:
    def __init__(self):
        self.head = None

    def new_block(self, data):

        if self.head is None:
            self.head = Block(data, 0)
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = Block(data, current.hash)

    def print_chain(self):
        if self.head is None:
            print("Empty Blockchain!!")
            return False
        else:
            current = self.head
            block_num = 0
            while current is not None:
                print("-----------------------------------------------")
                print("Block Number: {}".format(block_num))
                print("Timestamp: {}".format(current.timestamp))
                print("Data: {}".format(current.data))
                print("SHA256 Hash: {}".format(current.hash))
                print("Previous Hash: {}".format(current.previous_hash))

                block_num += 1
                current = current.next


republican_presidents = Blockchain()
# One edge case: printing empty chain
republican_presidents.print_chain()
republican_presidents.new_block("Donald J Trump")
republican_presidents.new_block("George W Bush")
republican_presidents.new_block("George HW Bush")
republican_presidents.new_block("Ronald Reagan")
republican_presidents.new_block("Gerald Ford")
republican_presidents.new_block("Richard Nixon")
republican_presidents.print_chain()
