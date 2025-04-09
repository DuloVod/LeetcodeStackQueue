from collections import deque

class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.stacks = {}
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        frequency = self.freq.get(val, 0) + 1
        self.freq[val] = frequency

        if frequency > self.max_freq:
            self.max_freq = frequency
            self.stacks[frequency] = deque()

        self.stacks[frequency].append(val)

    def pop(self):
        """
        :rtype: int
        """
        stack_with_max_freq = self.stacks[self.max_freq]

        val = stack_with_max_freq.pop()

        self.freq[val] -= 1

        if not stack_with_max_freq:
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
