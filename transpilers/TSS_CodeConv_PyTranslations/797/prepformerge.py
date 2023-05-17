import math

class prepformerge:
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
    def main(args):
        br = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        st = java.util.StringTokenizer(br.readLine())
        n = int(st.nextToken())
        lists = []
        a = [0 for _ in range(n + 1)]
        st = java.util.StringTokenizer(br.readLine())
        for i in range(1, n + 1):
            a [i] = int(st.nextToken())
        for i in range(1, n + 1):
            if i == 1:
                start = []
                start.append(a [i])
                lists.append(start)
            else:
                lo = 0
                hi = len(lists) - 1
                if lists[hi][len(lists[hi]) - 1] > a [i]:
                    start = []
                    start.append(a [i])
                    lists.append(start)
                else:
                    while lo != hi:
                        mid = math.trunc((lo + hi) / float(2))
                        if lists[mid][len(lists[mid]) - 1] < a [i]:
                            hi = mid
                        else:
                            lo = mid + 1
                    lists[lo].append(a [i])
        for lis in lists:
            for i, unusedItem in enumerate(lis):
                print(str(lis[i]) + " ", end = '')
            print()
