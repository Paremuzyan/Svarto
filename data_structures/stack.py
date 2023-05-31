class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push_item(self, element):
        self.stack.append(element)

    def pop_item(self):
        popped_elemet = self.stack[-1]
        del self.stack[-1]
        return popped_elemet

    def top(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def empty(self):
        return self.size == 0


stack = Stack()
for i in range(1, 10):
    stack.push_item(i)
print(stack)
for i in range(4):
    print(stack.pop_item())
stack.push_item(11)
stack.push_item(12)
print(stack)
