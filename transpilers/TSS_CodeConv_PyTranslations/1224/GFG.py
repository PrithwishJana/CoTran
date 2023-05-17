class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countSubarrays(arr, n):
        difference = 0
        ans = 0
        hash_positive = [0 for _ in range(n + 1)]
        hash_negative = [0 for _ in range(n + 1)]
        hash_positive [0] = 1
        for i in range(0, n):
            if (arr [i] & 1) == 1:
                difference += 1
            else:
                difference -= 1
            if difference < 0:
                ans += hash_negative [- difference]
                hash_negative [- difference] += 1
            else:
                ans += hash_positive [difference]
                hash_positive [difference] += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [3, 4, 6, 8, 1, 10, 5, 7]
        n = len(arr)
        print("Total Number of Even-Odd" + " subarrays are " + str(GFG.countSubarrays(arr, n)))
