class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_as_head(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print('prev_node must be linkedlist')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=' -> ')
            node = node.next
        print('None')

    def delete(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        while previous_node.next != target_node_data:
            previous_node = previous_node.next

        previous_node.next = previous_node.next.next



l = LinkedList()
first = Node(1)
l.head = first
second = Node(2)
first.next = second
third = Node(3)
second.next = third
l.insert_as_head('New Head')
l.insert_after(second, 5)
l.delete(third)

l.print_list()

