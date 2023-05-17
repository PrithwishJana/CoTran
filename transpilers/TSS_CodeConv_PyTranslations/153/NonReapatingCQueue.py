class NonReapatingCQueue:
    MAX_CHAR = 26
    @staticmethod
    def firstNonRepeating(str):
        charCount = [0 for _ in range(NonReapatingCQueue.MAX_CHAR)]
        q = java.util.LinkedList()
        i = 0
        while i < len(str):
            ch = str[i]
            q.add(ch)
            charCount [ch - 'a'] += 1
            while not q.isEmpty():
                if charCount [q.peek() - 'a'] > 1:
                    q.remove()
                else:
                    print(q.peek() + " ", end = '')
                    break
            if q.isEmpty():
                print(str(- 1) + " ", end = '')
            i += 1
        print()
    @staticmethod
    def main(args):
        str = "aabc"
        NonReapatingCQueue.firstNonRepeating(str)
