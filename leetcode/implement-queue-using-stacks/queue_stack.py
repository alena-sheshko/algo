"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack_push.append(x)

    def _flush(self):
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())

    def pop(self):
        """
        :rtype: nothing
        """
        self._flush()
        return self.stack_pop.pop()

    def peek(self):
        """
        :rtype: int
        """
        self._flush()
        return self.stack_pop[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not (self.stack_push or self.stack_pop)
