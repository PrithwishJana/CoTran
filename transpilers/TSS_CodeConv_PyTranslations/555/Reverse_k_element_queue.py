class Reverse_k_element_queue:
    queue = None
    @staticmethod
    def reverseQueueFirstKElements(k):
        if Reverse_k_element_queue.queue.isEmpty() == True or k > Reverse_k_element_queue.queue.size():
            return
        if k <= 0:
            return
        stack = java.util.Stack()
        for i in range(0, k):
            stack.push(Reverse_k_element_queue.queue.peek())
            Reverse_k_element_queue.queue.remove()
        while not stack.empty():
            Reverse_k_element_queue.queue.add(stack.peek())
            stack.pop()
        i = 0
        while i < Reverse_k_element_queue.queue.size() - k:
            Reverse_k_element_queue.queue.add(Reverse_k_element_queue.queue.peek())
            Reverse_k_element_queue.queue.remove()
            i += 1
    @staticmethod
    def Print():
        while not Reverse_k_element_queue.queue.isEmpty():
            print(Reverse_k_element_queue.queue.peek() + " ", end = '')
            Reverse_k_element_queue.queue.remove()
    @staticmethod
    def main(args):
        Reverse_k_element_queue.queue = java.util.LinkedList()
        Reverse_k_element_queue.queue.add(10)
        Reverse_k_element_queue.queue.add(20)
        Reverse_k_element_queue.queue.add(30)
        Reverse_k_element_queue.queue.add(40)
        Reverse_k_element_queue.queue.add(50)
        Reverse_k_element_queue.queue.add(60)
        Reverse_k_element_queue.queue.add(70)
        Reverse_k_element_queue.queue.add(80)
        Reverse_k_element_queue.queue.add(90)
        Reverse_k_element_queue.queue.add(100)
        k = 5
        Reverse_k_element_queue.reverseQueueFirstKElements(k)
        Reverse_k_element_queue.Print()
