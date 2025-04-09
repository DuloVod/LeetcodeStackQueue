class MyStack(object):

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            element = self.queue1.pop(0)
            self.queue2.append(element)

        top_element = self.queue1.pop(0)

        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element
        

    def top(self):
        """
        :rtype: int
        """
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            element = self.queue1.pop(0)
            self.queue2.append(element)

        top_element = self.queue1[0]

        self.queue2.append(self.queue1.pop(0))

        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
