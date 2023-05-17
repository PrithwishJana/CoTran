class solution:
    @staticmethod
    def no_of_ways(s):
        n = len(s)
        count_left = 0
        count_right = 0
        for i in range(0, n):
            if s[i] == s[0]:
                count_left += 1
            else:
                break
        for i in range(n - 1, -1, -1):
            if s[i] == s[n - 1]:
                count_right += 1
            else:
                break
        if s[0] == s[n - 1]:
            return ((count_left + 1) * (count_right + 1))
        else:
            return (count_left + count_right + 1)
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        s = "geeksforgeeks"
        print(solution.no_of_ways(s))
