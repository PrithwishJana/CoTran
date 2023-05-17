class GFG:
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def countPairs(arr, n):
        count = 0
        right = 0
        left = 0
        visited = [False for _ in range(n)]
        for i in range(0, n):
            visited [i] = False
        while right < n:
            while right < n and not visited [arr [right]]:
                count += (right - left)
                visited [arr [right]] = True
                right += 1
            while left < right and (right != n and visited [arr [right]]):
                visited [arr [left]] = False
                left += 1
        return count
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        arr = [1, 4, 2, 4, 3, 2]
        n = len(arr)
        print(GFG.countPairs(arr, n))
