class Solution:
    def numJewelsInStones(self, J, S):
        result = 0
        jHash = java.util.HashSet()
        j = 0
        while j < len(J):
            jHash.add(J[j])
            j += 1
        s = 0
        while s < len(S):
            if jHash.contains(S[s]):
                result += 1
            s += 1
        return result
    @staticmethod
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        sObj = Solution()
        J = "aA"
        S = "aAAbbbb"
        out = sObj.numJewelsInStones(J, S)
        print(out)
