class Solution:
    def minMoves(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        min_num = nums [0]
        ans = 0
        for num in nums:
            ans += num - min_num
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        nums = [1, 2, 3]
        out = sObj.minMoves(nums)
        print(out)
