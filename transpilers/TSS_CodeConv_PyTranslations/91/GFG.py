class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def maxSubArraySum(arr, size):
        max_so_far = arr [0]
        curr_max = arr [0]
        for i in range(1, size):
            curr_max = max(arr [i], curr_max + arr [i])
            max_so_far = max(max_so_far, curr_max)
        return max_so_far
    @staticmethod
    def lenOfLongSubarrWithGivenSum(arr, n, k):
        um = {}
        sum = 0
        maxLen = 0
        for i in range(0, n):
            sum += arr [i]
            if sum == k:
                maxLen = i + 1
            if sum in um.keys():
                um[sum] = i
            if sum - k in um.keys():
                if maxLen < (i - um[sum - k]):
                    maxLen = i - um[sum - k]
        return maxLen
    @staticmethod
    def lenLongSubarrWithMaxSum(arr, n):
        maxSum = GFG.maxSubArraySum(arr, n)
        return GFG.lenOfLongSubarrWithGivenSum(arr, n, maxSum)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [5, - 2, - 1, 3, - 4]
        n = len(arr)
        print("Length of longest subarray " + "having maximum sum = " + str(GFG.lenLongSubarrWithMaxSum(arr, n)))
