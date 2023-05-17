class AntonAndLines:
    eps = 10e-9
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws NumberFormatException, java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        n = int(br.readLine())
        st = java.util.StringTokenizer(br.readLine())
        start = float(st.nextToken())
        end = float(st.nextToken())
        first = []
        second = []
        for i in range(0, n):
            st = java.util.StringTokenizer(br.readLine())
            a = float(st.nextToken())
            b = float(st.nextToken())
            y1 = a * (start + AntonAndLines.eps) + b
            y2 = a * (end - AntonAndLines.eps) + b
            first.append(Pair(i + 1, y1, y2))
            second.append(Pair(i + 1, y2, y1))
        first.sort()
        second.sort()
        for i, unusedItem in enumerate(first):
            if first[i].id != second[i].id:
                print("YES")
                return
        print("NO")
    class Pair(Comparable):
        def __init__(self, i, a, b):
            #instance fields found by Java to Python Converter:
            self.x1 = 0
            self.x2 = 0
            self.id = 0

            self.x1 = a
            self.x2 = b
            self.id = i
        def compareTo(self, o):
            return (float(self.x1)).compareTo(o.x1)
