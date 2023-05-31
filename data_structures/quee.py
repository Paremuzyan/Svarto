class Queue:

    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.queue:
            popped_element = self.queue[0]
            del self.queue[0]
            return popped_element
        else:
            return 'The queue is empty!'

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return 'The queue is empty!'

    def rear(self):
        if self.queue:
            return self.queue[-1]
        else:
            return 'The queue is empty!'


if __name__ == "__main__":
    q = Queue()
    q.enqueue('Poghos')
    q.enqueue('Petros')
    q.enqueue('Patric')
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


