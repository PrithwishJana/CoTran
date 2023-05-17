class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        result = Integer.MIN_VALUE
        for house in houses:
            index = java.util.Arrays.binarySearch(heaters, house)
            if index < 0:
                index = - (index + 1)
            dist1 = house - heaters [index - 1] if index - 1 >= 0 else Integer.MAX_VALUE
            dist2 = heaters [index] - house if index < len(heaters) else Integer.MAX_VALUE
            result = max(result, min(dist1, dist2))
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        houses = [1, 2, 3]
        heaters = [2]
        out = sObj.findRadius(houses, heaters)
        print(out)
