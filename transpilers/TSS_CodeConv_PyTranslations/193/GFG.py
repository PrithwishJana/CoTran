class GFG:
    @staticmethod
    def minimumSubarrays(ar, n):
        se = []
        cnt = 1
        for i in range(0, n):
            if ar [i] in se == False:
                se.append(ar [i])
            else:
                cnt += 1
                se.clear()
                se.append(ar [i])
        return cnt
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        ar = [1, 2, 1, 3, 4, 2, 4, 4, 4]
        n = len(ar)
        print(GFG.minimumSubarrays(ar, n))
