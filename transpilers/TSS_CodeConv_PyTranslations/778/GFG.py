class GFG:
    @staticmethod
    def longestSubseq(s):
        n = len(s)
        pre_count_0 = [0 for _ in range(n + 2)]
        pre_count_1 = [0 for _ in range(n + 1)]
        post_count_0 = [0 for _ in range(n + 2)]
        pre_count_0 [0] = 0
        post_count_0 [n + 1] = 0
        pre_count_1 [0] = 0
        for j in range(1, n + 1):
            pre_count_0 [j] = pre_count_0 [j - 1]
            pre_count_1 [j] = pre_count_1 [j - 1]
            post_count_0 [n - j + 1] = post_count_0 [n - j + 2]
            if s[j - 1] == '0':
                pre_count_0 [j] += 1
            else:
                pre_count_1 [j] += 1
            if s[n - j] == '0':
                post_count_0 [n - j + 1] += 1
        if pre_count_0 [n] == n or pre_count_0 [n] == 0:
            return n
        ans = 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                ans = max(pre_count_0 [i - 1] + pre_count_1 [j] - pre_count_1 [i - 1] + post_count_0 [j + 1], ans)
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "000011100000"
        print(GFG.longestSubseq(s))
