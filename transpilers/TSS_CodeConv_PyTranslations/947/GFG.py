class GFG:
    @staticmethod
    def _minBroadcastRange(houses, towers):
        n = len(houses)
        m = len(towers)
        leftTower = Integer.MIN_VALUE
        rightTower = towers [0]
        j = 0
        k = 0
        min_range = 0
        while j < n:
            if houses [j] < rightTower:
                left = houses [j] - leftTower
                right = rightTower - houses [j]
                local_max = left if left < right else right
                if local_max > min_range:
                    min_range = local_max
                j += 1
            else:
                leftTower = towers [k]
                if k < m - 1:
                    k += 1
                    rightTower = towers [k]
                else:
                    rightTower = Integer.MAX_VALUE
        return min_range
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        a = [12, 13, 11, 80]
        b = [4, 6, 15, 60]
        max = GFG._minBroadcastRange(a, b)
        print(max)
