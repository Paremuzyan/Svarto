class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push_item(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop_item(self):
        if self.head is None:
            return

        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def top(self):
        if self is None:
            return

        else:
            return self.head.data

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=' -> ')
            node = node.next
        print('None')

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

