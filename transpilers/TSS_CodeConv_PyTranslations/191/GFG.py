class GFG:
    @staticmethod
    def longest_subseq(n, k, s):
        dp = [0 for _ in range(n)]
        max_length = [0 for _ in range(26)]
        for i in range(0, n):
            curr = s[i] - 'a'
            lower = max(0, curr - k)
            upper = min(25, curr + k)
            j = lower
            while j < upper + 1:
                dp [i] = max(dp [i], max_length [j] + 1)
                j += 1
            max_length [curr] = max(dp [i], max_length [curr])
        ans = 0
        for i in dp:
            ans = max(i, ans)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeksforgeeks"
        n = len(s)
        k = 3
        print(GFG.longest_subseq(n, k, s))
