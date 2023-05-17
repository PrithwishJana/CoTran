class GfG:
    @staticmethod
    def minSwaps(arr):
        n = len(arr)
        arrpos = []
        for i in range(0, n):
            arrpos.append(Pair  (arr [i], i))
        arrpos.sort(ComparatorAnonymousInnerClass())
        vis = [False for _ in range(n)]
        Arrays.fill(vis, False)
        ans = 0
        for i in range(0, n):
            if vis [i] or arrpos[i].getValue() == i:
                continue
            cycle_size = 0
            j = i
            while not vis [j]:
                vis [j] = True
                j = arrpos[j].getValue()
                cycle_size += 1
            if cycle_size > 0:
                ans += (cycle_size - 1)
        return ans

    class ComparatorAnonymousInnerClass(Comparator):
        def compare(self, o1, o2):
            if o1.getKey() > o2.getKey():
                return 1
            elif o1.getKey() is o2.getKey():
                return 0
            else:
                return - 1
class MinSwaps:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [1, 5, 4, 3, 2]
        g = GfG()
        print(GfG.minSwaps(a))
