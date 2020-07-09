class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    union = set()

    if llist_1.head is not None:
        current = llist_1.head
        while current is not None:
            union.add(current.value)
            current = current.next

    if llist_2.head is not None:
        current = llist_2.head
        while current is not None:
            union.add(current.value)
            current = current.next
    union_list = list(union)
    if len(union) == 0:
        print("Empty Union Set!!")
        return
    else:
        linked_list = LinkedList()

        for i in sorted(union_list):
            linked_list.append(i)
        return linked_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    set_1 = set()
    set_2 = set()

    if llist_1.head is not None:
        current = llist_1.head
        while current is not None:
            set_1.add(current.value)
            current = current.next

    if llist_2.head is not None:
        current = llist_2.head
        while current is not None:
            set_2.add(current.value)
            current = current.next

    intersection_list = list(set_1.intersection(set_2))

    if len(intersection_list) == 0:

        return "Empty Intersection Set!!"
    else:
        linked_list = LinkedList()
        for i in sorted(intersection_list):
            linked_list.append(i)
        return linked_list


# Test case 1
print("==========TEST CASE 1==========")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2
print("==========TEST CASE 2==========")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

print("==========TEST CASE 3==========")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1]
element_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
print(intersection(linked_list_5, linked_list_6))

print("==========TEST CASE 4==========")
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
print(intersection(linked_list_7, linked_list_8))
