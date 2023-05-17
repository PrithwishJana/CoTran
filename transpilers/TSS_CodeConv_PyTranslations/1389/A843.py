class A843:
    @staticmethod
    def main(args):
        in_ = java.util.Scanner(System.in)
        N = in_.nextInt()
        P = [None for _ in range(N)]
        for n in range(0, N):
            P [n] = java.awt.Point(n, in_.nextInt())
        java.util.Arrays.sort(P, ComparatorAnonymousInnerClass())
        output = StringBuilder()
        lineCount = 0
        used = [False for _ in range(N)]
        for n in range(0, N):
            if not used [n]:
                lineCount += 1
                count = 0
                pos = n
                line = StringBuilder()
                while not used [pos]:
                    count += 1
                    used [pos] = True
                    line.append(' ').append(pos + 1)
                    pos = P [pos].x
                output.append(count).append(line).append('\n')
        print(lineCount)
        print(output, end = '')

    class ComparatorAnonymousInnerClass(java.util.Comparator):
        def compare(self, o1, o2):
            return o1.y - o2.y
