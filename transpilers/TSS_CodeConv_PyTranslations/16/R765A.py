class R765A:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws Exception
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        st = java.util.StringTokenizer(br.readLine())
        t = int(st.nextToken())
#JAVA TO PYTHON CONVERTER WARNING: An assignment within expression was extracted from the following statement:
#ORIGINAL LINE: while (t -- > 0)
        while t  > 0:
            t -= 1
            st = java.util.StringTokenizer(br.readLine())
            n = int(st.nextToken())
            arr = [0 for _ in range(n)]
            st = java.util.StringTokenizer(br.readLine())
            for i in range(0, n):
                arr [i] = int(st.nextToken())
            R765A._solve(arr)
        t -= 1
    class Diff:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.prev = 0

    @staticmethod
    def _solve(arr):
        max = - 1
        map = {}
        i = 0
        while i < len(arr):
            if arr [i] in map.keys():
                diff = map[arr [i]]
                prev = diff.prev
                count = prev + len(arr) - i
                if count > max:
                    max = count
                diff.prev = i
            else:
                diff = Diff()
                diff.prev = i
                map[arr [i]] = diff
            i += 1
        print(max)
