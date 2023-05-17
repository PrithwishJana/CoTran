class Solution:
    nodeColors = None
    visited = None
    neighborstring = None
    startIndices = None
    edgesToPrint = None
    mod = 998244353
    parents = None
    cycleSet = None
    neighborPriority = None
    minPointsToEnterRoom = None
    maxPointsToEnterRoom = None
    pointOfEachRoom = None
    neighbors = None
    self._memo = None
    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: public static void main(String [] args) throws java.io.IOException
#JAVA TO PYTHON CONVERTER TASK: Python does not allow method overloads:
    def main(args):
        bufferedReader = java.io.BufferedReader(java.io.InputStreamReader(System.in))
        count = int(bufferedReader.readLine())
        pos = 0
        for i in range(0, count):
            s = bufferedReader.readLine().split(" ")
            no = int(s [0])
            if s [1] == "South":
                pos += no
                if pos > 20000:
                    break
            elif s [1] == "North":
                pos -= no
                if pos < 0:
                    break
            else:
                if pos == 0 or pos == 20000:
                    pos = 1
                    break
        if pos == 0:
            print("YES")
        else:
            print("NO")
