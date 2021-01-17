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
            current.next_node, current, previous = previous, current.next_node, current
            # next_node = current.next_node
            # current.next_node = previous
            # previous = current
            # current = next_node
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
            current.next_node, current, previous = previous, current.next_node, current
            # next_node = current.next_node
            # current.next_node = previous
            # previous = current
            # current = next_node
        self.head.next_node = previous

    def add_node(self, node: Node):
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = node

    def has_cycle(self) -> bool:
        fast = self.head
        slow = self.head
        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node
            if slow == fast:
                return True
        return False

    def remove_nth_fte(self, num: int):  # num > 0
        fast = self.head
        slow = self.head
        for i in range(0, num):
            fast = fast.next_node
            if fast is None:
                raise Exception('Out of limit')
        while fast.next_node:
            fast = fast.next_node
            slow = slow.next_node
        slow.next_node = slow.next_node.next_node

    def get_middle_node(self):
        fast = self.head
        slow = self.head
        while fast and fast.next_node:
            slow, fast = slow.next_node, fast.next_node.next_node
        return slow


def test_get_middle_node():
    linked_list = GuardedLinkedList()
    print(linked_list.get_middle_node())
    linked_list.add(1)
    print(linked_list.get_middle_node())
    linked_list.add(2)
    print(linked_list.get_middle_node())
    linked_list.add(3)
    print(linked_list.get_middle_node())
    linked_list.add(4)
    print(linked_list.get_middle_node())
    linked_list.add(5)
    print(linked_list.get_middle_node())


def test_remove_nth_fte():
    linked_list = GuardedLinkedList()
    linked_list.add(1)
    linked_list.remove_nth_fte(1)
    print(linked_list)

    linked_list.add(1)
    linked_list.add(2)
    print(linked_list)
    linked_list.remove_nth_fte(2)
    print(linked_list)
    linked_list.remove_nth_fte(1)

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)
    linked_list.add(4)
    linked_list.add(5)
    print(linked_list)
    linked_list.remove_nth_fte(1)
    print(linked_list)
    linked_list.remove_nth_fte(4)
    print(linked_list)


def test_reverse():
    linked_list = LinkedList()

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


def test_cycle_check():
    linked_list = GuardedLinkedList()
    print("Empty has cycle: ", linked_list.has_cycle())

    node1 = Node(1)
    linked_list.add_node(node1)
    node1.next_node = node1
    print("1 element has cycle: ", linked_list.has_cycle())

    # node2 = Node(2)
    # linked_list.add_node(node2)
    # print("2 element has cycle: ", linked_list.has_cycle())
    #
    # node2.next_node = node1
    # print("2 element has cycle: ", linked_list.has_cycle())


def merge_two_ordered_linked_list():
    linked_list_1 = GuardedLinkedList()
    linked_list_1.add(1)
    linked_list_1.add(2)
    linked_list_1.add(2)
    linked_list_1.add(7)
    linked_list_1.add(19)

    linked_list_2 = GuardedLinkedList()
    linked_list_2.add(0)
    linked_list_2.add(3)
    linked_list_2.add(7)
    linked_list_2.add(10)

    node1 = linked_list_1.head
    node2 = linked_list_2.head.next_node

    while node2:
        if node1.next_node is None:
            node1.next_node, node2.next_node, node1, node2 = node2, None, node2, None  # 把node2塞到list1的末尾，后面的连带过去了就不用再循环了
        elif node1.next_node.data > node2.data:  # 优化 实现node的比较大小，能处理data为None的情况
            node1.next_node, node2.next_node, node1, node2 = node2, node1.next_node, node2, node2.next_node
        else:
            node1 = node1.next_node
    print(linked_list_1)


if __name__ == '__main__':
    # test_reverse()
    # test_cycle_check()
    # merge_two_ordered_linked_list()
    # test_remove_nth_fte()
    test_get_middle_node()
