class GFG:
    @staticmethod
    def print_max(a, n, k):
        max_upto = [0 for _ in range(n)]
        s = Stack()
        s.push(0)
        for i in range(1, n):
            while (not s.empty()) and a [s.peek()] < a [i]:
                max_upto [s.peek()] = i - 1
                s.pop()
            s.push(i)
        while not s.empty():
            max_upto [s.peek()] = n - 1
            s.pop()
        j = 0
        i = 0
        while i <= n - k:
            while j < i or max_upto [j] < i + k - 1:
                j += 1
            print(str(a [j]) + " ", end = '')
            i += 1
        print()
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [9, 7, 2, 4, 6, 8, 2, 1, 5]
        n = len(a)
        k = 3
        GFG.print_max(a, n, k)
