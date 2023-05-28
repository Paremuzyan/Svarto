class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_data(self, new_data):
        if self.data:
            if new_data > self.data:
                if self.left is None:
                    self.left = Node(new_data)
                else:
                    self.left.insert_data(new_data)
            else:
                if self.right is None:
                    self.right = Node(new_data)
                else:
                    self.right.insert_data(new_data)
        else:
            self.data = Node(new_data)

    def print_tree(self):
        print(self.data)
        if self.left:
            self.left.print_tree()

        if self.right:
            self.right.print_tree()



root = Node(12)
root.insert_data(6)
root.insert_data(14)
root.insert_data(3)
# print(root.left.data)
root.print_tree()

