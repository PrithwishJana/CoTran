class Solution:
    def checkPossibility(self, nums):
        brokenPoint = 0
        i = 0
        while i < len(nums) - 1:
            if nums [i] > nums [i + 1]:
                brokenPoint += 1
                if brokenPoint >= 2:
                    return False
                if i - 1 < 0 or nums [i - 1] <= nums [i + 1]:
                    nums [i] = nums [i + 1]
                else:
                    nums [i + 1] = nums [i]
            i += 1
        return True
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        nums = [4, 2, 3]
        out = sObj.checkPossibility(nums)
        print(out)
