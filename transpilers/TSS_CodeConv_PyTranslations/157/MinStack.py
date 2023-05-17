class MinStack:
    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._stack = None
        self._minStack = None

        self._stack = Stack()
        self._minStack = Stack()
    def push(self, x):
        self._stack.push(x)
        if self._minStack.size() == 0 or x <= self._minStack.peek():
            self._minStack.push(x)
        else:
            self._minStack.push(self._minStack.peek())
    def pop(self):
        self._stack.pop()
        self._minStack.pop()
    def top(self):
        return self._stack.peek()
    def getMin(self):
        return self._minStack.peek()
    @staticmethod
    def main(args):
        m = MinStack()
        m.push(- 2)
        m.push(0)
        m.push(- 3)
        print(m.getMin())
        m.pop()
        print(m.top())
        print(m.getMin())
