class MyQueue(object):

    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_enqueue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        return -1

    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        if self.stack_dequeue:
            return self.stack_dequeue[-1]
        return -1

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack_enqueue and not self.stack_dequeue



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
