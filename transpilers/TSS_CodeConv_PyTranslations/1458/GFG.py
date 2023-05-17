class GFG:
    @staticmethod
    def MinCostTree(arr, n):
        ans = 0
        st = list  ()
        st.append(Integer.MAX_VALUE)
        for i in range(0, n):
            while st[len(st) - 1] <= arr [i]:
                x = st[len(st) - 1]
                st.pop(len(st) - 1)
                ans += x * min(st[len(st) - 1], arr [i])
            st.append(arr [i])
        for i in range(2, len(st)):
            ans += st[i] * st[i - 1]
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, 2, 3]
        n = len(arr)
        print(GFG.MinCostTree(arr, n), end = '')
