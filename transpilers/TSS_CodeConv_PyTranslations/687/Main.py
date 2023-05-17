class Solution:
    def findKthLargest(self, nums, k):
        self._shuffle(nums)
        k = len(nums) - k
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int j = partition(nums, lo, hi);
            j = self._partition(nums, lo, hi)
            if j < k:
                lo = j + 1
            elif j > k:
                hi = j - 1
            else:
                break
        return nums [k]
    def _partition(self, a, lo, hi):
        i = lo
        j = hi + 1
        while True:
#JAVA TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by Java to Python Converter:
#ORIGINAL LINE: while (i < hi && less(a [++ i], a [lo]));
            while i < hi and self._less(a [++ i], a [lo]):
                pass
#JAVA TO PYTHON CONVERTER TASK: The following assignment within expression was not converted by Java to Python Converter:
#ORIGINAL LINE: while (j > lo && less(a [lo], a [-- j]));
            while j > lo and self._less(a [lo], a [-- j]):
                pass
            if i >= j:
                break
            self._exch(a, i, j)
        self._exch(a, lo, j)
        return j
    def _exch(self, a, i, j):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int tmp = a [i];
        tmp = a [i]
        a [i] = a [j]
        a [j] = tmp
    def _less(self, v, w):
        return v < w
    def _shuffle(self, a):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Random random = new Random();
        random = Random()
        ind = 1
        while ind < len(a):
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final int r = random.nextInt(ind + 1);
            r = random.nextInt(ind + 1)
            self._exch(a, ind, r)
            ind += 1
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        out = sObj.findKthLargest(nums, k)
        print(out)
