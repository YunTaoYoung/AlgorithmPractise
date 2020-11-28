class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __str__(self):
        return self.data.__str__() if self.data is not None else 'None'


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = Node(data)

    def __str__(self):
        list_str = '['
        current = self.head
        while current is not None:
            list_str += current.__str__()
            if current.next_node is not None:
                list_str += ', '
            current = current.next_node
        list_str += ']'
        return list_str

    def reverse(self):
        current = self.head
        previous = None
        if current is None:
            return
        while current is not None:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous


class GuardedLinkedList:

    def __init__(self):
        self.head = Node(None)

    def add(self, data):
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = Node(data)

    def __str__(self):
        list_str = '['
        current = self.head.next_node
        while current is not None:
            list_str += current.__str__()
            if current.next_node is not None:
                list_str += ', '
            current = current.next_node
        list_str += ']'
        return list_str

    def reverse(self):
        current = self.head.next_node
        previous = None
        while current is not None:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head.next_node = previous


if __name__ == '__main__':
    linked_list = GuardedLinkedList()

    print(linked_list)
    linked_list.reverse()
    print(linked_list)

    linked_list.add('1')
    print(linked_list)
    linked_list.reverse()
    print(linked_list)

    linked_list.add(None)
    print(linked_list)
    linked_list.reverse()
    print(linked_list)

    linked_list.add('2 ')
    print(linked_list)
    linked_list.reverse()
    print(linked_list)
