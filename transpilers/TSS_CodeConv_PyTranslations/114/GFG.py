class GFG:
    @staticmethod
    def run_tasks(A, B):
        total_time = 0
        while not A.isEmpty():
            x = A.peek()
            y = B.peek()
            if x == y:
                A.remove()
                B.remove()
                total_time += 1
            else:
                A.remove()
                A.add(x)
                total_time += 2
        return total_time
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        A = LinkedList()
        A.add(3)
        A.add(2)
        A.add(1)
        A.add(4)
        B = LinkedList()
        B.add(4)
        B.add(1)
        B.add(3)
        B.add(2)
        print(GFG.run_tasks(A, B))
