import sys
from collections import deque


# re-using codex from the jupyter notebook exercises

class Node(object):

    def __init__(self, element=None, frequency=0, left=None, right=None):
        self.element = element
        self.frequency = frequency
        self.left = left
        self.right = right

    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element

    def set_frequency(self, value):
        self.frequency = value

    def get_frequency(self):
        return self.frequency

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


def connect_nodes(node_deque):
    if len(node_deque) == 1:
        child = node_deque.pop()

        root = Node()
        root.set_frequency(1)
        root.set_left_child(child)
        return root

    while len(node_deque) > 1:
        first_tree = node_deque.popleft()
        second_tree = node_deque.popleft()

        if first_tree.get_frequency() > second_tree.get_frequency():
            node_deque.append(first_tree)
            first_tree = node_deque.popleft()

        tree_node = Node()

        tree_node.set_left_child(first_tree)
        tree_node.set_right_child(second_tree)

        total_freq = tree_node.get_left_child().get_frequency() + tree_node.get_right_child().get_frequency()
        tree_node.set_frequency(total_freq)
        node_deque.appendleft(tree_node)

    return node_deque.pop()


def create_new_node(frequency_map):
    lst = list()

    for character, freq in frequency_map.items():
        new_node = Node(character, freq)
        lst.append(new_node)

    return deque(sorted(lst, key=lambda x: x.get_frequency()))


class HuffmanTree:

    def __init__(self, data=None):
        self.data = data
        self.root = None
        self.create_new_tree()

    def get_root(self):
        return self.root

    def create_new_tree(self):
        if self.data == '':
            print("Please enter a non-empty string!!")
            raise ValueError("Please enter a non-empty string!!")
        frequency_map = self.create_frequency_distribution()
        node_deque = create_new_node(frequency_map)
        self.root = connect_nodes(node_deque)

    def create_frequency_distribution(self):

        frequency_map = dict()

        for element in self.data:
            if element in frequency_map:
                frequency_map[element] += 1
            else:
                frequency_map[element] = 1

        return frequency_map


def recursive_search_tree(element, root):
    if root.get_element() == element:
        return ''

    left = None
    right = None

    if root.has_left_child():
        left = recursive_search_tree(element, root.get_left_child())

    if root.has_right_child():
        right = recursive_search_tree(element, root.get_right_child())

    if left is not None:
        return '0' + left

    if right is not None:
        return '1' + right


def huffman_encoding(data):
    tree = HuffmanTree(data)
    root = tree.get_root()
    encoded_data = ''

    for character in data:
        encoded_data += recursive_search_tree(character, root)

    return encoded_data, tree.get_root()


def huffman_decoding(codex, root):
    return huffman_decoding_recursive(codex, root, root, '', 0)


def huffman_decoding_recursive(codex, root, child, data, index):
    if not child.has_left_child() and not child.has_right_child():
        data += child.get_element()
        return huffman_decoding_recursive(codex, root, root, data, index)

    if index >= len(codex):
        return data

    bit = codex[index]
    if bit == '0':
        return huffman_decoding_recursive(codex, root, child.get_left_child(), data, index + 1)
    else:
        return huffman_decoding_recursive(codex, root, child.get_right_child(), data, index + 1)


def testing_function(a_great_sentence="The bird is the word"):
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))
    print("================================================================")
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    print("================================================================")
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


print("==========^^^^^^^^^^ DEFAULT TEST ^^^^^^^^^^===========")
testing_function()
print("==========^^^^^^^^^^ TEST 1 ^^^^^^^^^^===========")
testing_function("Agustuz")
print("==========^^^^^^^^^^ TEST 2 ^^^^^^^^^^===========")
testing_function("aaaaaa")
print("==========^^^^^^^^^^ TEST 3 ^^^^^^^^^^===========")
testing_function("Bears, beets, Battlestar Galactica")

