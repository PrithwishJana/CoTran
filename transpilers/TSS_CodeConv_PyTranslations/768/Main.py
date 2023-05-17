class Solution:
    def maxAreaOfIsland(self, grid):
        dr = [1, - 1, 0, 0]
        dc = [0, 0, 1, - 1]
        ans = 0
        r0 = 0
        while r0 < len(grid):
            c0 = 0
            while c0 < len(grid [0]):
                if grid [r0][c0] == 1:
                    shape = 0
                    stack = java.util.Stack()
                    stack.push([r0, c0])
                    grid [r0][c0] = 0
                    while not stack.empty():
                        node = stack.pop()
                        r = node [0]
                        c = node [1]
                        shape += 1
                        for k in range(0, 4):
                            nr = r + dr [k]
                            nc = c + dc [k]
                            if 0 <= nr and nr < len(grid) and 0 <= nc and nc < len(grid [0]) and grid [nr][nc] == 1:
                                stack.push([nr, nc])
                                grid [nr][nc] = 0
                    ans = max(ans, shape)
                c0 += 1
            r0 += 1
        return ans
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        grid = [[ 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 ], [ 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 ], [ 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0 ], [ 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 ], [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 ]]
        out = sObj.maxAreaOfIsland(grid)
        print(out)
