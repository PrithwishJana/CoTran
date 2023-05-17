class SlidingWindow:
    @staticmethod
    def printMax(arr, n, k):
        Qi = java.util.LinkedList()
        i = 0
        for i in range(0, k):
            while (not Qi.isEmpty()) and arr [i] >= arr [Qi.peekLast()]:
                Qi.removeLast()
            Qi.addLast(i)
        while i < n:
            print(str(arr [Qi.peek()]) + " ", end = '')
            while (not Qi.isEmpty()) and Qi.peek() <= i - k:
                Qi.removeFirst()
            while (not Qi.isEmpty()) and arr [i] >= arr [Qi.peekLast()]:
                Qi.removeLast()
            Qi.addLast(i)
            i += 1
        print(arr [Qi.peek()])
    @staticmethod
    def main(args):
        arr = [12, 1, 78, 90, 57, 89, 56]
        k = 3
        SlidingWindow.printMax(arr, len(arr), k)
