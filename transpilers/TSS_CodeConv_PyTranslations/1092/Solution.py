class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [0 for _ in range(n)]
        res [0] = 1
        for i in range(1, n):
            res [i] = res [i - 1] * nums [i - 1]
        right = 1
        for i in range(n - 1, -1, -1):
            res [i] *= right
            right *= nums [i]
        return res
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        nums = [1, 2, 3, 4]
        out = sObj.productExceptSelf(nums)
        print(Arrays.toString(out))
