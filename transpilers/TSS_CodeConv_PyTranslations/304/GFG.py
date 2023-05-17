class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxLength(s, n):
        ans = Integer.MIN_VALUE
        A = list  ()
        L = list  ()
        R = list  ()
        freq = [0 for _ in range(n + 5)]
        for i in range(0, 26):
            count = 0
            for j in range(0, n):
                if s[j] - 'a' == i:
                    count += 1
                freq [j] = count
            for j in range(1, n):
                L.append((2 * freq [j - 1]) - j)
                R.append((2 * freq [j]) - j)
            max_len = Integer.MIN_VALUE
            min_val = Integer.MAX_VALUE
            for j, unusedItem in enumerate(L):
                min_val = min(min_val, L[j])
                A.append(min_val)
                l = 0
                r = j
                while l <= r:
                    mid = (l + r) >> 1
                    if A[mid] <= R[j]:
                        max_len = max(max_len, j - mid + 1)
                        r = mid - 1
                    else:
                        l = mid + 1
            ans = max(ans, max_len)
            A.clear()
            R.clear()
            L.clear()
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "ababbbacbcbcca"
        n = len(s)
        print(GFG.maxLength(s, n))
