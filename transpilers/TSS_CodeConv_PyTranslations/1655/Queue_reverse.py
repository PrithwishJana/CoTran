class Queue_reverse:
    queue = None
    @staticmethod
    def Print():
        while not Queue_reverse.queue.isEmpty():
            print(Queue_reverse.queue.peek() + " ", end = '')
            Queue_reverse.queue.remove()
    @staticmethod
    def reverseQueue(q):
        if q.isEmpty():
            return q
        data = q.peek()
        q.remove()
        q = Queue_reverse.reverseQueue(q)
        q.add(data)
        return q
    @staticmethod
    def main(args):
        Queue_reverse.queue = java.util.LinkedList()
        Queue_reverse.queue.add(56)
        Queue_reverse.queue.add(27)
        Queue_reverse.queue.add(30)
        Queue_reverse.queue.add(45)
        Queue_reverse.queue.add(85)
        Queue_reverse.queue.add(92)
        Queue_reverse.queue.add(58)
        Queue_reverse.queue.add(80)
        Queue_reverse.queue.add(90)
        Queue_reverse.queue.add(100)
        Queue_reverse.queue = Queue_reverse.reverseQueue(Queue_reverse.queue)
        Queue_reverse.Print()
