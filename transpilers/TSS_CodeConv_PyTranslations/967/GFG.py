class GFG:
    @staticmethod
    def waysToSplit(s):
        n = len(s)
        answer = 0
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        seen = [0 for _ in range(26)]
        for i in range(0, n):
            prev = (prefix [i - 1] if i - 1 >= 0 else 0)
            if seen [s[i] - 'a'] == 0:
                prefix [i] += (prev + 1)
            else:
                prefix [i] = prev
            seen [s[i] - 'a'] = 1
        for i in range(0, 26):
            seen [i] = 0
        suffix [n - 1] = 0
        for i in range(n - 1, 0, -1):
            prev = suffix [i]
            if seen [s[i] - 'a'] == 0:
                suffix [i - 1] += (prev + 1)
            else:
                suffix [i - 1] = prev
            seen [s[i] - 'a'] = 1
        for i in range(0, n):
            if prefix [i] == suffix [i]:
                answer += 1
        return answer
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "ababa"
        print(GFG.waysToSplit(s))
